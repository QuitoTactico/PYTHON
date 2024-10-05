def sumaGrupos(nums: list, k: int) -> bool:
    return sum2(nums, k, "", "")


# def f(n:list,k:int,l:list) -
def sum2(nums: list, k: int, l: str, n: str) -> str:
    if k == 0:
        r1 = list(map(int, str(l).split()))
        r2 = list(map(int, str(n).split()))
        r2.extend(nums)
        r1.sort()
        r2.sort()
        res = [r1, r2]
        return res
    if len(nums) == 0:
        return False
    else:  # codigo mamawebo
        a = sum2(nums[1:], k, l, n + " " + str(nums[0]))
        b = sum2(nums[1:], k - nums[0], l + " " + str(nums[0]), n)
        if a == False:
            return b  # si el monitor lee esto, escríbale al 301 725 2587. le debe una mamada
        if b == False:
            return a
        if a == False and b == False:
            return False  # easter egg para el monitor
        return a  # blowjob


# n = list(map(int,input().split()))
# n=[80, 59 , 60 , 81 , 57 , 58 , 76 , 75]

# print(k)


n = int(input())
nums = [0] * n
for i in range(n):
    nums[i] = int(input())


"""l = list(map(int,sumaGrupos(nums,k)[0].split()))
print(l)
r = list(map(int,sumaGrupos(nums,k)[1].split()))
print(r)
#print(sumaGrupos(nums,k)[1])"""
"""print(n)
print(nums)
print(k)"""


def s(n: list) -> int:
    if len(n) == 1:
        return n[0]
    return n[0] + s(n[1:])


# print(sumaGrupos(n,k))
def equilibra(personas):
    k = s(personas) // 2
    return sumaGrupos(personas, k)


print(equilibra(nums))
