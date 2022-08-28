d = {}
def brit(n):
    d[n] , mid  = [] , int((n-1)/2) 
    for i in range(n):
        if i == mid : 
            d[n].append(["+"]*mid + ["#"] + ["+"]*mid)
            continue
        temp , temp[i], temp[n-1-i], temp[mid]= ["0"]*n , "#" , "#" , "+"
        d[n].append(temp)
for r in range (5,26,2): brit(r)
for _ in range(int(input())):
    temp2 = []
    m = int(input())
    for k in range(m): temp2.append(list(input()))
    if temp2 == d[m]:print("Bandera britanica")
    else: print("Ni idea")
