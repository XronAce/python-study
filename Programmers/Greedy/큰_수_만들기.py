def solution(number, k):
    numlist = list(map(int, number))
    delCnt = 0
    while delCnt < k:
        for i in range(0, len(numlist)-1):
            if numlist[i] < numlist[i+1]:
                numlist[i] = 10
                delCnt += 1
                if delCnt == k:
                    break
                
    for i in range(0, k):
        numlist.remove(10)

    answer = "".join(map(str, numlist))
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


number = "1231234"
k = 3
print(solution(number, k))