s = "MCMXCIV"


def romanToInt(s) -> int:
    romandic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0

    # for i in range(len(s)-1):
    #     print('a= '+str(s[i])+' b= '+str(s[i+1]))
    #     if romandic[s[i]] < romandic[s[i+1]]:
    #         result -= romandic[s[i]]
    #     else:
    #         result += romandic[s[i]]
    # return result + romandic[s[-1]]

    for a, b in zip(s, s[1:]):
        print('a= '+str(a)+' b= '+str(b))
        if romandic[a] < romandic[b]:
            result -= romandic[a]
        else:
            result += romandic[a]
    return result + romandic[s[-1]]


print(romanToInt(s))
