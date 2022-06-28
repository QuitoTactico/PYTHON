h, m = int(input()), int(input())
rh = 11-h if m != 0 else 12-h
if rh == 0 : rh = 12
rm = 60-m if m != 0 else 0
print(f'{rh}:{rm}')