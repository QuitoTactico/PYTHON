s = input()
a = int(input())
b = int(input())
if b > len(s):
    print("Error")
elif a > b:
    print("Error2")
else:
    print(s[a : b + 1])
