strs = ["ab", "a"]


def longestCommonPrefix(strs) -> str:
    prefix = strs[0]

    for str in strs[1:]:
        while str[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if len(prefix) == 0:
                return ''
    return prefix


print(longestCommonPrefix(strs))
