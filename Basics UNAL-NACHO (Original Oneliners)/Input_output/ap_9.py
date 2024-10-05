import math
res = (math.pi *(float(input()) ** 2) * float(input())) - (float(input())*float(input()))
if res < 0 : res = 0
print(round(res,3))