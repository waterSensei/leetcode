nums = [1, 2, 3, 1]


def containsDuplicate(nums) -> bool:
    return not len(set(nums)) == len(nums)


containsDuplicate(nums)
