def solution(name):
    alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1}
    # 우방향, 좌방향 탐색 시 연속되는 A의 갯수를 판별. A갯수가 적은 방향으로 탐색해야 하며, 갯수가 같을 경우 어디 방향이든 상관없음. (탐욕법적 사고)
    partialName = list(name[1:])
    rev_partialName = list(reversed(partialName))

    rightCnt = 0
    leftCnt = 0
    for i in range(0, len(partialName)):
        if partialName[i] == 'A':
            rightCnt += 1
        else:
            break
    
    for i in range(0, len(rev_partialName)):
        if rev_partialName[i] == 'A':
            leftCnt += 1
        else:
            break

    answer = 0
    # 왼쪽방향으로 진행 시
    if rightCnt > leftCnt:
        rev_partialName.insert(0, name[0])
        print(rev_partialName)
        for i in range(0, len(rev_partialName)):
            answer += alphabet[rev_partialName[i]]
        answer += len(rev_partialName) - 1
        if rightCnt != 0:
            answer -= rightCnt
    #오른쪽방향으로 진행 시
    else:
        partialName.insert(0, name[0])
        print(partialName)
        for i in range(0, len(partialName)):
            answer += alphabet[partialName[i]]
        answer += len(partialName) - 1
        if leftCnt != 0:
            answer -= leftCnt

    return answer

# name = "JEEAN"
# print(solution(name))

"""
탐욕법적 사고로 저렇게 생각했는데
테스트케이스가 온전히 통과되지 않습니다.
name = "BBABAAAABBBAAAABABB" 이런경우에는 오른방향 탐색 중 좌방향 탐색을 한다는 등 탐색 방향을 중간에 틀어야 최단 입력이 되는 경우가 있습니다.
이걸 Greedy 문제로 풀 수 없다는게 제 개인 관점이고, 따라서 여기서 Greedy 문제 풀이를 종료합니다.
"""