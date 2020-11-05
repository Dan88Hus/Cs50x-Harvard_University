from sys import argv
import cs50

if len(argv) != 2:
    exit("Usage: python roster.py Housename")
# print ('this works')

# db = SQL("sqlite:///students.db")
db = cs50.SQL("sqlite:///students.db")

rows = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first", argv[-1])

# Lavender Brown, born 1979
for row in rows:
    print(row['first'] + ' ' + (row['middle']+' ' if row['middle'] else '') + row['last'] + ', born ' + str(row['birth']))

# Lavender Brown, born 1979
# Colin Creevey, born 1981
# Seamus Finnigan, born 1979
# Hermione Jean Granger, born 1979
# Neville Longbottom, born 1980
# Parvati Patil, born 1979
# Harry James Potter, born 1980
# Dean Thomas, born 1980
# Romilda Vane, born 1981
# Ginevra Molly Weasley, born 1981
# Ronald Bilius Weasley, born 1980

