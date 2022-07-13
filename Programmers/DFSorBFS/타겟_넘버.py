from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)]) # sum, level
    while queue:
        s, l = queue.popleft()
        if l > len(numbers):
            break
        elif l == len(numbers) and s == target:
            answer += 1
        queue.append((s+numbers[l-1], l+1))
        queue.append((s-numbers[l-1], l+1))

    return answer

numbers = [1, 2, 3, 4, 5]
target = 3
print(solution(numbers, target))

"""
Used BFS(Breath-First Search) with queue.
"""