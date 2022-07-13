from collections import deque

def Draw(matrix): # 그려주는 함수
    for i in range(0, len(matrix)):
        print(matrix[i])

def solution(rows, columns, queries):
    # 행렬 그리기
    answer = []
    matrix = []
    temp = 1
    for i in range(0, rows):
        innerMatrix = []
        for j in range(0, columns):
            innerMatrix.append(temp)
            temp += 1
        matrix.append(innerMatrix)
    # print("original")
    # Draw(matrix)
    # print("\n")

    # 매 회전마다 최저 수 구하기
    queries = deque(queries)
    while queries:
        changedElement = []
        (x1, y1) = (queries[0][0]-1, queries[0][1]-1)
        (x2, y2) = (queries[0][2]-1, queries[0][3]-1)
        # 상 테두리 회전 작업
        temp = matrix[x1+1][y1]
        temp1 = matrix[x1][y2]
        for i in range(y2, y1, -1):
            matrix[x1][i] = matrix[x1][i-1]
            changedElement.append(matrix[x1][i])
        matrix[x1][y1] = temp
        changedElement.append(matrix[x1][y1])
        # print("top cycle")
        # Draw(matrix)
        # print("\n")
        
        # 우 테두리 회전 작업
        temp = matrix[x2][y2]
        for i in range(x2, x1, -1):
            matrix[i][y2] = matrix[i-1][y2]
            changedElement.append(matrix[i][y2])
        matrix[x1+1][y2] = temp1
        changedElement.append(matrix[x1+1][y2])
        # print("right cycle")
        # Draw(matrix)
        # print("\n")

        # 하 테두리 회전작업
        temp1 = matrix[x2][y1]
        for i in range(y1, y2):
            matrix[x2][i] = matrix[x2][i+1]
            changedElement.append(matrix[x2][i])
        matrix[x2][y2-1] = temp
        changedElement.append(matrix[x2][y2-1])
        # print("bottom cycle")
        # Draw(matrix)
        # print("\n")

        # 좌 테두리 회전작업
        for i in range(x1+1, x2):
            matrix[i][y1] = matrix[i+1][y1]
            changedElement.append(matrix[i][y1])
        matrix[x2-1][y1] = temp1
        changedElement.append(matrix[x2-1][y1])
        # print("left cycle")
        # Draw(matrix)
        # print("\n")
        
        # Draw(matrix)
        # print("\n")
        answer.append(min(changedElement))
        queries.popleft()
    
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))