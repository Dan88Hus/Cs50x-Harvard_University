import cs50
import sys
import csv

# this part check for argv elements count
if len(sys.argv) != 2:
    exit("Usage: python import.py characters.csv")
print("This works :) ")
# this line connects oython to database
db = cs50.SQL("sqlite:///students.db")
# this part insert into database and split name cells to 3 cells
with open(sys.argv[-1], 'r') as characters:
    reader = csv.DictReader(characters)
    for row in reader:
        house = row['house']
        birth = row['birth']
        curr_name = row['name'].split()
        first, middle, last = curr_name[0], curr_name[1] if len(curr_name) == 3 else None, curr_name[-1]
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", first, middle, last, house, birth)
        # print("done")
    print("OK")

