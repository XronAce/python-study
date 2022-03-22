def max_product(left_cards, right_cards):
    max = 0
    for i in range(0, len(left_cards)):
        for j in range(0, len(right_cards)):
            temp = left_cards[i]*right_cards[j]
            if temp > max:
                max = temp
    return max
    
# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))