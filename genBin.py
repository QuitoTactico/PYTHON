from collections import deque
def binarios(n):
    bin = deque()
    for i in range(1,n+1):
        b = ""
        if i == 1 :
            bin.append("1")
            continue
        while True:
            b = str(i%2) + b
            i = i//2
            if i == 1 or i == 0: 
                b = str(i%2) + b
                break
        bin.append(b)
    print(list(bin))

def agregarBinario(i : int):
    b = ""
    while True:
        b = str(i%2) + b
        i = i//2
        if i == 1 or i == 0: 
            b = str(i%2) + b
            break
    print(b)

    '''for a in range(1,i+1):
        b = ""
        while True:
            b = b + str(a%2)
            a = a//2
            if a == 1 or a == 2 or a == 0: 
                b = str(a%2)
                break
        print(b)
        #i = h'''

    
n = int(input())
binarios(n)

#agregarBinario(n)
#print(deque())