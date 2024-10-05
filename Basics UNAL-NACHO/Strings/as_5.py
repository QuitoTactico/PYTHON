for _ in range(int(input())):
    s, l = "", list(map(str, input().split("_")))
    for i in l:
        s = s + i[0].upper() + i[1:]
    print(s)
