from cs50 import get_int


while True:
    h = get_int("Height:")
    if h > 0 and h <= 8:
        break

# print_hash = "#"
# for i in range(1,h+1):
#     print((h-i)*" ", i*print_hash)

for i in range(h):
    for j in range(h):
        if i+j >= h-1:
            print("#", end="")
        else:
            print(" ", end="")
    print()
