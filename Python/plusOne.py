digits = [1, 2, 3]


def plusOne(digits) -> list:
    s = ''
    for i in digits:
        s += str(i)
    return [int(x) for x in str(int(s)+1)]


print(plusOne(digits))
