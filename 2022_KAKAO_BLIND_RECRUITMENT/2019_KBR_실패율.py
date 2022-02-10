def solution(N, stages):
    failRate = {}
    denominator = len(stages)
    
    for i in range(1, N+1):
        numerator = 0
        for stage in stages:
            if stage == i:
                numerator += 1
        if denominator == 0: # To avoid ZeroDivisionError -> This will cause Runtime Error if not considered.
            failRate[i] = 0
        else:
            failRate[i] = numerator/denominator
        denominator -= numerator

    sort_desc_failRate = dict(sorted(failRate.items(), key=lambda x:x[1], reverse=True))
    answer = list(sort_desc_failRate.keys())

    return answer

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# print(solution(N, stages))