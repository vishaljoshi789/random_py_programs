lst = list([])
y = int(input("how many numbers you need to print : "))

for e in range(1, y+1):
    x = int(input("Enter numbers : "))
    print("You have entered", e, "numbers")
    lst.append(x)
i = 0
j = 0
for z in lst:
    if z%2 == 0:
        print(z, "is a even number")
        i+= 1
    else:
        print(z, "is a odd number")
        j+=1

print("There are", i, "even numbers and", j, "odd numbers")
