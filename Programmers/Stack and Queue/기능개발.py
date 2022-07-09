def solution(progresses, speeds):
    if (100-progresses[0]) % speeds[0] != 0:
        queue = [[(100-progresses[0]) // speeds[0] + 1, 1]]
    else:
        queue = [[(100-progresses[0]) // speeds[0], 1]]
    for i in range(1, len(progresses)):
        if (100-progresses[i]) % speeds[i] != 0:
            dayLeft = (100-progresses[i]) // speeds[i] + 1
        else:
            dayLeft = (100-progresses[i]) // speeds[i]
        if queue[-1][0] < dayLeft:
            queue.append([dayLeft, 1])
        else:
            queue[-1][1] += 1
    
    answer = []
    for i in range(0, len(queue)):
        answer.append(queue[i][1])

    return answer

# progresses = [93, 30, 55]
# progresses = [96, 94]
# speeds = [1, 30, 5]
# speeds = [3, 3]
# print(solution(progresses, speeds))