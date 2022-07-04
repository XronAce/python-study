from itertools import permutations
from math import sqrt

def solution(numbers):
    numlist = list(map(int, numbers))
    numPossible = []
    cnt = 0

    permutationList = []
    for i in range(1, len(numlist)+1):
        temp = list(map(list, permutations(numlist, i)))
        for j in range(0, len(temp)):
            if temp[j] not in permutationList:
                permutationList.append(temp[j])
 
    for i in range(0, len(permutationList)):
        if int("".join(map(str, permutationList[i]))) == 1:
            continue
        elif int("".join(map(str, permutationList[i]))) == 0:
            continue
        elif int("".join(map(str, permutationList[i]))) not in numPossible:
            numPossible.append(int("".join(map(str, permutationList[i]))))

    print(numPossible)
    
    for i in range(0, len(numPossible)):
        isPrime = 1
        for j in range(2, int(sqrt(numPossible[i]) + 1)):
            if numPossible[i] % j == 0:
                isPrime = 0
        if isPrime == 1:
            cnt += 1
            
    answer = cnt
    return answer

# numbers = "011"
# print(solution(numbers))

"""
1. Create list that contains all possible numbers out of given numbers.
2. Prime number checking algorithm required. Lessen execution time by adapting sqrt.
"""