def rotate(nums, k) -> None:
    k = k % len(nums)
    if k == 0:
        return
    a = nums[-k:]
    b = nums[0:len(nums)-k]
    nums[:] = a + b
    return


print(rotate([1], 0))
