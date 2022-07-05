def solution(n, lost, reserve):
    # 체육복 여벌이 있던 학생이 도둑맞은 경우
    lost_hasReserve = []
    new_lost = []
    new_reserve = []
    
    for i in range(1, n+1):
        if i in lost and i in reserve:
            lost_hasReserve.append(i)
    
    for i in range(0, len(lost)):
        if lost[i] not in lost_hasReserve:
            new_lost.append(lost[i])
    
    for i in range(0, len(reserve)):
        if reserve[i] not in lost_hasReserve:
            new_reserve.append(reserve[i])

    # 각 학생별 체육복을 빌릴 수 있는 사람의 수 구하기
    PossibleReserve = {} # {학생: 빌릴수있는 가짓수}
    for i in range(0, len(new_lost)):
        PossibleReserve[new_lost[i]] = 0
        if new_lost[i] - 1 in new_reserve:
            PossibleReserve[new_lost[i]] += 1
        if new_lost[i] + 1 in new_reserve:
            PossibleReserve[new_lost[i]] += 1
    
    # 가짓수로 오름차순 정렬
    sort_PossibleReserve = sorted(PossibleReserve.items(), key = lambda item: item[1])

    # sort_PossibleReserve 기재된 순으로 먼저 빌리기. 매번 빌릴때마다 new_lost 와 new_reserve 업데이트 처리.
    for i in range(0, len(sort_PossibleReserve)):
        if sort_PossibleReserve[i][0] - 1 in new_reserve:
            new_lost.remove(sort_PossibleReserve[i][0])
            new_reserve.remove(sort_PossibleReserve[i][0] - 1)
            continue
        elif sort_PossibleReserve[i][0] + 1 in new_reserve:
            new_lost.remove(sort_PossibleReserve[i][0])
            new_reserve.remove(sort_PossibleReserve[i][0] + 1)
            continue

    # new_lost에 남아있는 사람 수만큼 n에서 뺀게 정답
    answer = n - len(new_lost)
    return answer

# n = 3
# lost = [3]
# reserve = [1]
# print(solution(n, lost, reserve))