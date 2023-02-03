nums1 = [1, 2, 2, 1]
nums2 = [2, 2]


def intersectV1(nums1, nums2) -> list:
    o = []
    for x in nums1:
        if (x in nums2):
            o.append(x)
            nums2.remove(x)
    return o


def intersectV2(nums1, nums2) -> list:
    d1 = {}
    for num in nums1:
        if num not in d1:
            d1[num] = 0
        d1[num] += 1
    d2 = {}
    for num in nums2:
        if num not in d2:
            d2[num] = 0
        d2[num] += 1
    result = []
    for key in d1.keys():
        if key in d2:
            for i in range(0, min(d1[key], d2[key])):
                result.append(key)
    return result


print(intersectV2(nums1, nums2))
