nums = [1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 5, 6]


def removeDuplicatesV1(nums) -> int:
    if len(nums) == 0:
        return 0
    new = [nums[0]]
    for x in range(len(nums)-1):
        if nums[x+1] != nums[x]:
            new.append(nums[x+1])
    nums[:] = new
    return len(nums)


def removeDuplicatesV2(nums) -> int:
    nums[:] = sorted(set(nums))
    return len(nums)


def removeDuplicatesV3(nums) -> int:
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


print(removeDuplicatesV2(nums))
print(nums)
