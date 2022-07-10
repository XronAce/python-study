from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 1
    truckOnBridge = deque([[truck_weights[0], 1]])
    remainingTruck = deque(truck_weights)
    remainingTruck.popleft()
    

    while remainingTruck:
        time += 1
        for i in range(0, len(truckOnBridge)):
            truckOnBridge[i][1] += 1
        
        if truckOnBridge[0][1] == bridge_length+1:
            truckOnBridge.popleft()
        
        currentWeight = 0
        for i in range(0, len(truckOnBridge)):
            currentWeight += truckOnBridge[i][0]
        
        if weight - currentWeight >= remainingTruck[0]:
            truckOnBridge.append([remainingTruck[0], 1])
            remainingTruck.popleft()

    answer = time + bridge_length
    return answer

# bridge_length = 2
# weight = 10
# truck_weights = [7,4,5,6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]
# print(solution(bridge_length, weight, truck_weights))