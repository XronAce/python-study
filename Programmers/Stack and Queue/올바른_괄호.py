def solution(s):
    if s[0] != '(':
        return False
    
    stack = []
    for i in range(0, len(s)):
        if stack == []:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.append(s[i])
        else:
            if stack[-1] == ')':
                return False
            stack.pop()
    
    if stack != []:
        return False

    return True

# s = "())()(()"
# print(solution(s))