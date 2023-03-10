x = 76


def mySqrt(x) -> int:
    l, r = 0, x
    while l < r:
        mid = (l+r) // 2
        if x < mid*mid:
            r = mid
        else:
            l = mid + 1
    return l-1 if l > 1 else l


print(mySqrt(x))
