def merge_the_tools(string, k):
    # your code goes here
    x = len(string)
    y = x//k
    o = k
    a = ''
    b = 0
    l = b
    m = k
    u = ''
    z = ''
    for i in range(y):
            a += string[b:k]
            for e in a[l:m]:
                if e not in z:
                    u += e
                    z += e
                else:
                    pass
            u += '\n'
            z = ''
            l = m
            m += o
            b = k
            k += o
    print(a)
    print(u)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
