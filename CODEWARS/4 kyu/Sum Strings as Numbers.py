def suma_aux(x, y):
    nothing = [None, "", " "]
    if x in nothing and y in nothing:
        return "0"
    if x in nothing:
        return y
    if y in nothing:
        return x

    if len(x) < len(y):
        x = ("0" * (len(y) - len(x))) + x
    elif len(x) > len(y):
        y = ("0" * (len(x) - len(y))) + y

    reversed_x, reversed_y = x[::-1], y[::-1]
    i = 0
    carry = 0
    sol = ""
    while True:
        # print(i)
        if i >= len(x) and i >= len(y):
            return sol + str(carry)

        suma = int(reversed_x[i]) + int(reversed_y[i]) + carry
        # print(suma)
        carry = 1 if suma >= 10 else 0
        suma = suma % 10
        sol = sol + str(suma)
        i += 1


def sum_strings(x, y):
    suma = suma_aux(x, y)[::-1]
    for i in suma:
        if i != "0":
            break
        else:
            suma = suma[1:]

    return suma if suma != "" else "0"


# "13333","1111121"
# print(sum_strings("1999","99"))
print(sum_strings("000012345", "111"))

"""
if __name__ == '__main__':
    x = "12345"
    y = "1111111111"
    reversed_a = x[::-1]

    print(reversed_a[1+1:][::-1])

    x = ('0'*(len(y)-len(x))) + x
    print(x)    
"""


# --------------------------------- smart one ------------------------------
def sum_strings(x, y):
    l, res, carry = max(len(x), len(y)), "", 0
    x, y = x.zfill(l), y.zfill(l)
    for i in range(l - 1, -1, -1):
        carry, d = divmod(int(x[i]) + int(y[i]) + carry, 10)
        res += str(d)
    return ("1" * carry + res[::-1]).lstrip("0") or "0"
