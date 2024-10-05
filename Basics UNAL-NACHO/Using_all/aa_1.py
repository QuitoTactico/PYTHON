for _ in range(int(input())):
    s, res = input().replace(" ", "").split(":"), "Es anagrama"
    for i in s[1]:
        if i in s[0]:
            s[0] = s[0].replace(i, "", 1)
        else:
            res = "No es anagrama"
            break
    if len(s[0]) != 0:
        res = "No es anagrama"
    print(res)
