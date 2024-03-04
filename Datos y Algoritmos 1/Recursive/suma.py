def sumar(n:int)->int:
    if(n==1):
        return 1
    return sumar(n-1)+n


def main():
    n=int(input())
    print(sumar(n))
    
main()