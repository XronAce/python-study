def solution(s):
    slist = list(s)
    stack = []
    for i in range(0, len(slist)):
        if stack == []:
            stack.append(slist[i])
        elif stack[-1] == slist[i]:
            stack.pop()
        else:
            stack.append(slist[i])
    print(stack)

    if len(stack) == 0:
        return 1
    else:
        return 0

# s = "baabaa"
# s = "cdcd"
# print(solution(s))