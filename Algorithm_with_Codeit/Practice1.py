def sublist_max(profits):
    max_profit = 0
    for i in range(0, len(profits)):
        for j in range(0, len(profits)):
            sub_profits = profits[i:j+1]
            sum = 0
            for k in sub_profits:
                sum += k
            if sum > max_profit:
                max_profit = sum

    return max_profit


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))