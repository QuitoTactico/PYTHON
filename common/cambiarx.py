def cantidad(s : str, n : int):
    if(n == len(s)):
        return ""
    if(s[n]=="x"):
        return "y"+ cantidad(s, n+1)
    return s[n]+cantidad(s, n+1)

s = input()
print(cantidad(s, 0))