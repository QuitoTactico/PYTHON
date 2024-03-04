def a(m,n): return n+1 if m == 0 else (a(m-1,1) if m > 0 and n == 0 else a(m-1,a(m,n-1)))
for i in range(int(input())): print(a(int(input()),int(input())))