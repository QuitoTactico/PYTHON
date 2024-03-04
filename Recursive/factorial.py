def factorial(n : int) -> int:
    if(n == 0):
        return 1
    return factorial(n-1)*n

def main():
    n = int(input())
    print(factorial(n))
    
main()