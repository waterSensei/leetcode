nums = [3, 3, 4]
target = 6


def twoSum(nums, target) -> list:
    l = {}
    for i in range(len(nums)):
        c = target - nums[i]
        if c in l:
            return [l[c], i]
        l[nums[i]] = i


print(twoSum(nums, target))
