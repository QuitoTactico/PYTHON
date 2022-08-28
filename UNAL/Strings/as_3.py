for _ in range(int(input())): 
    v = [False]*5
    for i in input():
        if i == "a": v[0] = True
        if i == "e": v[1] = True
        if i == "i": v[2] = True
        if i == "o": v[3] = True
        if i == "u": v[4] = True
    res = "Panvocalica" if False not in v else "No es panvocalica"
    print(res)