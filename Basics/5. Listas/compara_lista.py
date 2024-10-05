a = ["snbbbb", "sn", "sa", "s", "na", "nnnnnnn", "a", ""]
b = ["snbbbb", "sn", "sb", "s", "nb", "nnnnnnn", "b", ""]


def r(a, b, m):
    if len(a) == 0:
        return m
    return max(c(a[0], b, 0), r(a[1:], b, m))


def c(a: str, b, m) -> int:
    if len(b) == 0:
        return m
    if a == b[0]:
        m = max(m, len(a))
    return c(a, b[1:], m)


print(r(a, b, 0))
# print(c("b",a,0))
# a=[]
# print(len(a))
# print(max(5,6))
