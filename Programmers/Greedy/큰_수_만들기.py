def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while stack and num > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    
    if k != 0:
        stack = stack[:-k]
        print(stack)
    
    answer = "".join(map(str, stack))
    return answer

# number = "9876543"
# number = "1231234"
# number = "4177252841"
# k = 3
# print(solution(number, k))