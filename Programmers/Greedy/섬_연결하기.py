def solution(n, costs):
    costs.sort(key = lambda x:x[2])
    connected = [costs[0][0], costs[0][1]]
    MST = [costs[0][0], costs[0][1]]
    answer = costs[0][2]
    while len(MST) != n:
        for i in range(1, len(costs)):
            temp = [costs[i][0], costs[i][1]]
            if temp not in connected:
                connected.append(temp)
                for i in range(0, len(temp)):
                    if temp[i] not in MST:
                        MST.append(temp[i])
                answer += costs[i][2]``
            elif costs[i][0] in connected:
                answer += costs[i][2]
                connected.append(costs[i][1])
            elif costs[i][1] in connected:
                answer += costs[i][2]
                connected.append(costs[i][0])

    return answer

costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
costs = [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]]
n = 4
n = 5
print(solution(5, costs))