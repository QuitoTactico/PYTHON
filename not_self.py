a = [-1,1,0,-3,3]

def multip(a:list, n:int) -> int:
    c = 1
    for i in a[:n-1]+a[n:]:
        c = c * i
    return c


if __name__ == '__main__':
    b = []
    for i in range(len(a)):
        b.append(multip(a,i+1))

    print(b)


