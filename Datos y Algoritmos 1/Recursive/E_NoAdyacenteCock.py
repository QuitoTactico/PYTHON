def sumaGrupos(nums: list, k: int) -> bool:
    return sum2(nums, k, 0, [])


def sum2(nums: list, k: int, c: int, l: list):
    if c == len(nums):
        return k == 0
    else:
        return sum2(nums, k, c + 1, l) or sum2(
            nums,
            k - nums[c],
            c + 1,
        )


n = int(input())
nums = [0] * n
for i in range(n):
    nums[i] = int(input())
k = int(input())
print(sumaGrupos(nums, k))
