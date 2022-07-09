from collections import deque

def get_key(dict, val):
    for key, value in dict.items():
        if val == value:
            return key


def solution(priorities, location):
    temp = []
    num_priority = {}
    for i in range(0, len(priorities)):
        temp.append(i)
        num_priority[i] = priorities[i]
    deq = deque(temp)
    printqueue = []
    
    while deq:
        max_priority = 0
        for i in range(0, len(deq)):
            max_priority = max(max_priority, num_priority[deq[i]])
        for i in range(0, get_key(num_priority, max_priority)):
            temp = deq[0]
            deq.popleft()
            deq.append(temp)
        printqueue.append(deq[0])
        deq.popleft()

    return printqueue.index(location) + 1

priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))

"""
20/100, need to be fixed
"""