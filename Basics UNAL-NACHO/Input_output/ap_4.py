h, m,p = int(input()) , int(input()), input()
p = 'am' if h == 12 and p == 'pm' else 'pm' if h == 12 and p == 'am' else p
res = ((11-h)*60) + 60-m
res = res+720 if p == 'am' else 1440 if res == 0 else res
print(f'faltan {res} para las 12')