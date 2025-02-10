def longest_consecutive_subsequence(nums:list):
    if not nums: return 0
    if len(nums) == 1: return 1

    nums.sort()

    res = 1
    temp = 1
    last = nums[0]

    for item in nums[1:]:
        if item-last == 1:
            last = item
            temp += 1
        elif item == last:
            continue
        else:
            res = max(res, temp)
            temp = 1
        last = item

    return max(res, temp)