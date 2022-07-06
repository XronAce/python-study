from collections import deque

def solution(people, limit):
    deq = deque(sorted(people))
    
    boatCnt = 0
    while deq:
        if len(deq) == 1:
            boatCnt += 1
            deq.pop()
        elif deq[0] + deq[-1] <= limit:
            boatCnt += 1
            deq.pop()
            deq.popleft()
        else:
            boatCnt += 1
            deq.pop()
    
    answer = boatCnt
    return answer

# people = [70, 50, 80, 50]
# limit = 100
# print(solution(people, limit))

"""
Using deque made it faster than using a list.
This is because
list.pop() -> O(1)
list.pop(0) -> O(n)
deque.pop() -> O(1)
deque.popleft() -> O(1)
So in case of popping leftmost element, deque is faster than list. 
"""