def fib(n):
    a = 0
    b = 1

    for i in range(n):
        if a < n:
            print(a)

        else:
            break
        c = a+b
        a = b
        b = c


n = int(input("Enter the number : "))

fib(n)

