from math import factorial

def staircase(n):
    combinations = 0
    for i in range(0, n//2 + 1):
        if n == 0:
            return 1
        numof2 = i
        numof1 = n - 2*i
        
        combinations += factorial(numof1+numof2) / (factorial(numof2)*factorial(numof1))
    
    return int(combinations)


# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
