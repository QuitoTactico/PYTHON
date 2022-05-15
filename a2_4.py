def f(n): return 0 if n %123==0 else 1+f(n+23)
for i in range(int(input())): print(f(int(input())))