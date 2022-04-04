def select_stops(water_stops, capacity):
    water = capacity - water_stops[0]
    answer = []
    for i in range(0, len(water_stops)-1):
        next = water_stops[i+1] - water_stops[i]
        
        if water < next:
            water = capacity
            answer.append(water_stops[i])
            water -= next
        else:
            water -= next

    answer.append(water_stops[-1])
    return answer



# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))

"""
This problem uses Greedy Algorithm
1. It has Optimal Substructure: Choosing substructure between choosing when to fill the water
2. It has Greedy Choice Property: Going to the furthest water stops it could get to in every situations
"""