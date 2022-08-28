def p(n): return (2*n) + 1
def a(n): return 3**n
def n(n): return ((5*n)+4)**0.5
for i in range(int(input())): print(p(a(n(float(input())))))