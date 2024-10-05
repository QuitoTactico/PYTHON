# Salta el repetido
def sumaGrupos(nums: str, i: int) -> int:
    if len(nums) == 1:
        return i + int(nums[0])
    if len(nums) == 2:
        if nums[0] == nums[1]:
            return i
    if len(nums) > 2:
        if nums[0] == nums[1]:
            return sumaGrupos(nums[2:], i)
    return sumaGrupos(nums[1:], i + int(nums[0]))


nums = input()
print(sumaGrupos(nums, 0))
# que lindo código lmao
