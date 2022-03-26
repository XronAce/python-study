def consecutive_sum(start, end):
    mid = (start + end) // 2
    if start == end:
        return start
    else:
        return consecutive_sum(start, mid) + consecutive_sum(mid+1, end)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))

"""
Consecutive Sum in DP?
Split the sum into half using recursive function. There must be the difference between recursive sum and consecutive sum.
Divide and Conquer
1. Divide
2. Conquer
3. Combine
"""