def sublist_max(profits):
    start = 0
    for i in range(0, len(profits)):
        if profits[i] > 0:
            start = i
            break
    
    max_profit = 0
    total = 0
    for i in range(start, len(profits)):
        total += profits[i]
        max_profit = max(max_profit, total)
    
    return max_profit
                
    

# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))