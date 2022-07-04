def solution(answers):
    answer = []
    solutions = { 1: [1, 2, 3, 4, 5], 2: [2, 1, 2, 3, 2, 4, 2, 5], 3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    score = {}
    
    for solution in solutions.keys():
        cnt = 0
        if len(solutions[solution]) >= len(answers):
            for i in range(0, len(answers)):
                if solutions[solution][i] == answers[i]:
                    cnt += 1
            score[solution] = cnt
        else:
            for i in range(0, len(answers)):
                if answers[i] == solutions[solution][i%len(solutions[solution])]:
                    cnt += 1
            score[solution] = cnt

    sorted_score = sorted(score.items(), key = lambda item: item[1], reverse=True)
    
    maxScore = sorted_score[0][1]
    for i in range(0, len(sorted_score)):
        if sorted_score[i][1] == maxScore:
            answer.append(sorted_score[i][0])

    answer.sort()
    return answer

# answers = [1,3,2,4,2]
# print(solution(answers))