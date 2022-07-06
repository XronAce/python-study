
def solution(number, k):
    answer = number
    length = len(number)
    curLen = len(answer)

    while len(answer) != length-k:
        for i in range(0, len(answer)-1):
            if answer[i] < answer[i+1]:
                answer = answer[0:i] + answer[i+1:]
                break
        if len(answer) == curLen:
            answer = answer[:-1]
            curLen -= 1

    return answer

## Below is the bruteforcing method.

# from itertools import combinations

# def solution(number, k):
#     numlist = list(map(int, number))
#     idxlist = []
#     for i in range(0, len(number)):
#         idxlist.append(i)
    
#     elimIdx = list(combinations(idxlist, k))

#     possibleNum = []
#     for i in range(0, len(elimIdx)):
#         numlist = list(map(int, number))
#         for j in range(0, k):
#             numlist[elimIdx[i][j]] = 'X'
#         while 'X' in numlist:
#             numlist.remove('X')
#         possibleNum.append("".join(map(str, numlist)))
    
#     maxNum = possibleNum[0]
#     for i in range(0, len(possibleNum)):
#         maxNum = max(maxNum, possibleNum[i])
    
#     answer = maxNum

#     return answer


number = "9876543"
k = 3
print(solution(number, k))