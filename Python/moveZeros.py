nums = [0, 1, 0, 3, 12]


def moveZeroes(nums) -> None:
    a = []
    zeros = []
    for x in nums:
        if x == 0:
            zeros.append(x)
        else:
            a.append(x)
    nums[:] = a+zeros


moveZeroes(nums)
print(nums)
