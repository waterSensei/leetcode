nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


def merge(nums1, m, nums2, n) -> None:
    nums1[:] = sorted(nums1[:m]+nums2[:n])
    return None


merge(nums1, m, nums2, n)
print(nums1)
