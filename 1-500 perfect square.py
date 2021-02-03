
x = int(input("type the smaller number : "))
y = int(input("type the greater number : "))
for i in range(x, y+1):
    while i**2 < y:
        print(i, "=", i**2)
        i += 1

    break




