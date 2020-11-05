from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from datetime import datetime
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, usd

#initializer of flask
app = Flask(__name__)

#templates are re-loaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#configure cs50 to sql database
db = SQL("sqlite:///warehouse.db")


# Homepage
@app.route("/")
@login_required
def index():
    """Show all item list of stocks"""

    # Select symbol owned by user and its quantity
    item_list = db.execute("SELECT it_name, it_qnty, it_pur_price, it_pur_date, it_sal_price FROM item")

    item_list = item_list

# Print portfolio to index homepage
    return render_template("item.html", item_list=item_list)

# Warehouse List
@app.route("/warehouse_list")
@login_required
def warehouse():
    """Show all warehouses in table"""

    # Select
    warehouse_list = db.execute("SELECT lo_name, lo_address, lo_email FROM location")

    warehouse_list = warehouse_list

    # Print portfolio to index homepage
    return render_template("warehouse_list.html", warehouse_list=warehouse_list)


# Transfer List
@app.route("/transfer_list")
@login_required
def transferlist():
    """Show all item list of stocks"""

    # Select symbol owned by user and its quantity
    tr_list = db.execute("SELECT tr_lo, tr_time, tr_qnty, tr_shipping_cost, tr_item FROM transfer")

    tr_list = tr_list

# Print portfolio to index homepage
    return render_template("transfer_list.html", tr_list=tr_list)





# # records items
@app.route("/item_record", methods=["GET", "POST"])
@login_required
def it_record():
    """item record"""

    if request.method == "POST":
        name = request.form.get("it_name")
        pur_price = request.form.get("it_pur_price")
        sal_price = request.form.get("it_sal_price")
        qnty = request.form.get("it_qnty")
        date = request.form.get("it_pur_date")
        db.execute("INSERT INTO item (it_name, it_pur_price, it_sal_price, it_qnty, it_us_id, it_pur_date) VALUES (:it_name, :it_pur_price, :it_sal_price, :it_qnty, :it_us_id, :it_pur_date)", it_name = name, it_pur_price = pur_price, it_sal_price = sal_price, it_qnty = qnty, it_us_id = session["user_id"], it_pur_date = date)
        flash("recorded to item table")
    else:
        return render_template("item_record.html")
    return redirect("/item_record")


# Location records
@app.route("/location_record", methods=["GET", "POST"])
@login_required
def lo_record():
    """item record"""

    if request.method == "POST":
        name = request.form.get("lo_name")
        address = request.form.get("lo_address")
        email = request.form.get("lo_email")
        db.execute("INSERT INTO location (lo_name, lo_address, lo_email, lo_us_id) VALUES (:lo_name, :lo_address, :lo_email, :lo_us_id)", lo_name = name, lo_address = address, lo_email = email, lo_us_id = session["user_id"])
        flash("Recorded!")
    else:
        return render_template("location.html")
    return redirect("/location_record")





@app.route("/transfer", methods=["GET", "POST"])
@login_required
def transfer():
    """keep record of items transfer"""
    items = db.execute("SELECT it_name, it_qnty, it_id FROM item WHERE it_qnty >= 0")
    names = db.execute("SELECT lo_name, lo_address, lo_email FROM location")
    if request.method == "POST":

        qnty = request.form.get("tr_qnty")
        date = request.form.get("tr_time")
        tr_shipping_cost = request.form.get("tr_shipping_cost")

        selected_item = request.form.get("it_name")
        selected_tr_id = db.execute(("SELECT it_id FROM item WHERE it_name = :selected_item"), selected_item = selected_item)
        it_tr_id = selected_tr_id[0]["it_id"]
        selected_lo = request.form.get("lo_name")
        selected_lo_id = db.execute(("SELECT lo_id FROM location WHERE lo_name = :selected_lo"), selected_lo = selected_lo)
        lo_tr_id = selected_lo_id[0]["lo_id"]
        # print("selected location :", selected_lo)
        # print("selected location id:",lo_tr_id)



        # print ("inserted")
        ################# Update of the warehouse quantity on hand after transfer has been done###########
        it_qnty = db.execute(("SELECT it_qnty FROM item WHERE it_name = :selected_item"), selected_item = selected_item)
        selected_it_qnty = it_qnty[0]["it_qnty"]
        print(selected_it_qnty)
        if int(qnty) > int(selected_it_qnty):
            flash ("Negative stock is not allowed")
            return redirect("/transfer")
        else:
            db.execute("INSERT INTO transfer (tr_item, tr_lo, tr_qnty, tr_time, it_tr_id, lo_tr_id, tr_shipping_cost) VALUES (:tr_item, :tr_lo, :tr_qnty, :tr_time, :it_tr_id, :lo_tr_id, :tr_shipping_cost)", tr_item = selected_item, tr_lo = selected_lo, tr_qnty = qnty, tr_time = date, it_tr_id = it_tr_id, lo_tr_id = lo_tr_id, tr_shipping_cost = tr_shipping_cost)
            db.execute("UPDATE item SET it_qnty = (it_qnty - :qnty) WHERE it_id = :it_tr_id", qnty = qnty, it_tr_id = it_tr_id)
            flash ("Current Stock is Updated!")



    else:

        return render_template("transfer.html", items=items, names = names)


    return redirect("/transfer")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash ("No Username Entered")
            return redirect("/login")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash ("No Password Entered")
            return redirect("/login")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE us_name = :username",
                          username=request.form.get("username"))

        # print(rows[0]["us_hash"])

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["us_hash"], request.form.get("password")):
            flash ("Invalid Username/Password")
            return redirect("/login")

        # Remember which user has logged in
        session["user_id"] = rows[0]["us_id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        user_name = request.form.get("username")
        user_pass = request.form.get("password")
        pass_confirmation = request.form.get("confirmation")
        email = request.form.get("email")

        # Ensure username was submitted
        if not user_name:
            flash ("No Username")
            return redirect("/register")

        # Ensure password was submitted
        elif not user_pass:
            flash ("No password")
            return redirect("/register")

        # Ensure password confirmation was submitted
        elif not pass_confirmation:
            flash ("must provide password confirmation")
            return redirect("/register")

        # Ensure password and confirmation match
        elif user_pass != pass_confirmation:
            flash ("Passwords does not match")
            return redirect("/register")

        if db.execute("SELECT * FROM users WHERE us_name = :username", username = user_name):
            flash ("User name is taken")
            return redirect("/register")

        # Add username and hashed password to the database
        result = db.execute("INSERT INTO users (us_name, us_hash, us_email) VALUES (:username, :hash, :email)", username = user_name, hash = generate_password_hash(user_pass), email = email)

        # Ensure username is not already in database
        if not result:
            flash ("username already exists")
            return redirect("/register")

         # Remember which user has logged in
        session["user_id"] = result

        # message
        flash("Registered!-Welcome to Warehouse")

        # Redirect user to login form
        return redirect("/")

    else:
        return render_template("register.html")


