def find_missing_number(nums):
    return list(set(range(len(nums)+2)) - set(nums))[0] #unoptimal oneliner


print(find_missing_number([]))