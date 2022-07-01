def solution(board, moves):
    stack = []
    flag = 1
    answer = 0

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                break
    
    while flag == 1:
        flag = 0
        for i in range(len(stack)-1):
            if stack[i] == stack[i+1]:
                flag = 1
                answer += 1
                stack[i] = 0
                stack[i+1] = 0
        stack = [k for k in stack if k != 0]

    answer = answer*2

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))

"""
[0,0,0,0,0],
[0,0,1,0,3],
[0,2,5,0,1],
[4,2,4,4,2],
[3,5,1,3,1]
stack = [4,3,1,1,3,2,4]
answer = 4
"""