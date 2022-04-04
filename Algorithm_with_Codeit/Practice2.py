def power(x, y):
    if y == 0:
        return 1
    
    subresult = power(x, y // 2)
    if y % 2 == 1:
        return x * subresult * subresult
    else:
        return subresult * subresult


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))

"""
This algorithm uses Dynamic Programming
Overlapping Subproblems: subresult
"""