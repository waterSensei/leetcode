s = "[()]"


def isValid(s) -> bool:
    d = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for i in s:
        if i in d:
            stack.append(d[i])
        elif len(stack) == 0 or stack.pop() != i:
            return False
    return len(stack) == 0


print(isValid(s))
