def f():
    v, c, mc, co = [], [], True, True
    for i in range(5):
        v.append(int(input()))
        c.append(input())
    for i in c:
        if i != c[0]:
            mc = False
    v.sort()
    for i in range(1, len(v)):
        if v[i] != v[i - 1] + 1:
            co = False
    return (
        "Escalera real"
        if v[0] == 10 and mc == True
        else (
            "Escalera de color"
            if mc == True and co == True
            else (
                "Escalera normal"
                if co == True
                else ("Color" if mc == True else "Otra mano")
            )
        )
    )


for i in range(int(input())):
    print(f())
