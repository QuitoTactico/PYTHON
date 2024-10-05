def f(l: list, c, i):
    if c >= len(l) - 1:
        if l[i] < l[c]:
            i = c
        return i
    if l[i] < l[c]:
        i = c
    return f(l, c + 2, i)


# l = ["Calvarini",1000,"Pinturosky",2000,"Tajardini",400]
# print(f(l,1,1))


def mascorrupto(l: list):
    return l[f(l, 1, 1) - 1]


# mascorrupto(l)
