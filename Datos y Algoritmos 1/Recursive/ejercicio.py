# que belleza de código, estoy muy feliz
def f(n: int, list: list, c: int) -> int:
    if c == n:
        return 1
    if c > n:
        return 0
    for j in range(0, int(len(list)) - 1, 1):
        return f(n, [list.pop(j)], c + list[j])


def g(r: int) -> str:
    if (r == 0) or (r == None):
        return "False"
    return "True"


e = int(input())
list = [0 for i in range(e)]
for h in range(0, e, 1):
    list[h] = int(input())
n = int(input())

if (e == 0) and (e == n):
    print("True")
    quit()
for v in range(1, len(list), 1):
    if (list[v - 1] == 5) and (list[v] == 1):
        list[v] = 0
y = 0  # Contador con todos los multiplos de 5
for x in range(0, int(len(list)), 1):
    if list[x] % 5 == 0:
        y = y + list[x]
        list[x] = 0

print(f(n, list, y))
