from cs50 import get_float

quarter = 25
dime = 10
nickel = 5
pennie = 1
# //prompt the user for input as dollars in loop to control negative number
while (pennie == 1):
    dollars = get_float("Change owed:")
    if (dollars > 0):
        cents = int(dollars * 100)
        # print(cents)
        break


divider = 0
remain = 0
total_divider = 0
while (cents >= pennie):

    if (cents >= quarter):
        # print("this works")
        remain = cents % quarter
        # print(remain)
        # //calculate division
        divider = int(cents / quarter)
        # print(divider)
        total_divider = total_divider + divider
        # print(total_divider)

    elif (cents >= dime):
        remain = cents % dime
        # print(remain)
        # //calculate division
        divider = int(cents / dime)
        total_divider = total_divider + divider
        # print(total_divider)

    elif (cents >= nickel):
        remain = cents % nickel
        # //calculate division
        divider = int(cents / nickel)
        total_divider = total_divider + divider
        # print(total_divider)

    else:
        remain = cents % pennie
        # //calculate division
        divider = int(cents / pennie)
        total_divider = total_divider + divider
        # print(total_divider)

    cents = remain

print(f"{total_divider+cents}")

