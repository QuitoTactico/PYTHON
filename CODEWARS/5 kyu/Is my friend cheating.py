def remov_nb(n):
    sol = []
    #total = sum(range(n+1))
    total = (n*(n+1))//2

    for a in range(1, n+1):
        b = (total-a) // (a+1)

        if b * a == total-a-b and b <= n:
            sol.append((a,b))
        
        '''
        for b in rng:
            if total-a-b == a*b:
                sol.append((a,b))
        '''

    return sol

print(remov_nb(26)) # (15, 21), (21, 15)


'''

a*b = total-a-b

(a*b)+b = total-a

b*(a+1) = total-a

b = (total-a) / (a+1)

'''