def f(n: int, list: list, c: int) -> int:
    if c == n:
        return 1
    if c > n:
        return 0
    for j in range(0, int(len(list)) - 1, 1):
        return f(n, [list.pop(j)], c + list[j])


def g(r: int) -> str:
    if r == 0:
        return "NO"
    return "YES"


e, n = map(int, input().split())
list = list(map(int, input().split(" ")))
if e == 0:
    print("NO")
    quit()
print(len(list))
print(g(f(n, list, 0)))
