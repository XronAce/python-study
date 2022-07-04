from math import sqrt

def solution(brown, yellow):
    # Approach with yellow box
    maxDivisor = int(sqrt(yellow))
    rowcol_YPair = []

    # Getting pair of possible (row, column) of yellow box (Common Divisor)
    for i in range(1, maxDivisor+1):
        if yellow % i == 0:
            rowcol_YPair.append((yellow//i, i))
    
    # Brute forcing with given number of brown to check its perfect match.
    for pair in rowcol_YPair:
        numBrown = pair[0] * 2 + pair[1] * 2 + 4
        if numBrown == brown:
            answer = [pair[0]+2, pair[1]+2]
            break
    
    return answer

# brown = 24
# yellow = 24
# print(solution(brown, yellow))