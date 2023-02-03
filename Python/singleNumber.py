nums = [1, 0, 2, 0, 2]


def singleNumberV1(nums) -> int:
    nums = sorted(nums)
    for x in range(0, len(nums)-1, 2):
        if nums[x] != nums[x+1]:
            return nums[x]
    return nums[len(nums)-1]


def singleNumberV2(nums) -> int:
    a = 0
    for b in nums:
        a ^= b
    return a


print(singleNumberV2(nums))
