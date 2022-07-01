def solution(scoville, K):
    isAllOverK = 0
    answer = 0
    while isAllOverK == 0:
        scoville.sort(key=lambda x:x)
        if scoville[0] < K:
            temp = scoville[0] + scoville[1] * 2
            scoville.pop(0)
            scoville.pop(0)
            scoville.insert(0, temp)
            answer += 1
        for i in range(len(scoville)):
            if scoville[i] < K:
                isAllOverK = 0
                break;
            else:
                isAllOverK = 1
        if len(scoville) == 1:
            if scoville[0] < K:
                answer = -1
                isAllOverK = 1
    
    return answer

"""
테스트 케이스는 다 통과했으나 효율성에서 통과를 못함.
heapq를 써야 효율성을 통과할 수 있음.
"""