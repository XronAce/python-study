def max_crossing_sum(profits, start, end):
    mid_point = (start + end) // 2
    max_left = 0
    max_right = 0
    max_left_start = 0
    max_right_end = 0
    
    for i in range(0, mid_point+1):
        temp = max_left
        max_left = max(max_left, sum(profits[mid_point-i:mid_point+1]))
        if temp != max_left:
            max_left_start = mid_point-i
    
    for i in range(mid_point+1, end):
        temp = max_right
        max_right = max(max_right, sum(profits[mid_point+1:i+1]))
        if temp != max_right:
            max_right_end = i
    
    return sum(profits[max_left_start:max_right_end+1])


def sublist_max(profits, start, end):
    if start == end:
        return profits[start]
    
    mid = (start + end) // 2
    max_left = sublist_max(profits, start, mid)
    max_right = sublist_max(profits, mid+1, end)
    max_cross = max_crossing_sum(profits, start, end)
    return max(max_left, max_right, max_cross)
    

# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))