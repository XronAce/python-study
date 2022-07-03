def calAvgTime(jobs):
    currentTime = jobs[0][1]
    totalTime = jobs[0][1] - jobs[0][0]

    for i in range(1, len(jobs)):
        if currentTime > jobs[i][0]:
            totalTime += currentTime - jobs[i][0]
            totalTime += jobs[i][1]
            currentTime += jobs[i][1]
        elif currentTime == jobs[i][0]:
            totalTime += jobs[i][1]
            currentTime += jobs[i][1]
        else:
            totalTime += jobs[i][1]
            currentTime += jobs[i][0] - currentTime
            currentTime += jobs[i][1]
    
    return int(totalTime / len(jobs))

def solution(jobs):
    jobs.sort(key = lambda x: x[0])
    first = jobs[0]
    jobs.pop(0)
    jobs.sort(key = lambda x: x[1])
    jobs.insert(0, first)
    answer = calAvgTime(jobs)
    return answer

jobs = [[0, 3], [1, 9], [2, 6]]
jobs = [[0, 3], [2, 6], [1, 9]]
print(calAvgTime(jobs))
print(solution(jobs))