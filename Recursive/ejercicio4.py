def pali(s : str, t : str) -> bool:
    if(s == t):
        return True
    if(len(s) == len(t)):
        return False
    if(len(s) == len(t)+1):
        return pali(s,t+s[-1])
    return pali(s[0:int(len(s)-1)],t+s[-1])

s = input()

print(pali(s,""))
#creo que es el código más inteligente que he hecho hasta la fecha