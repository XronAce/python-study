def solution(s):
    answer = 1001
    quotient = []
    final = []

    for i in range(0, len(s)-1):
        quotient.append(i+1)

    for q in quotient:
        splice = []
        repTime = 1
        string = s
        for i in range(0, len(string), q):
            temp = string[i:i+q]
            splice.append(temp)

        for i in range(0, len(splice)-1):
            if splice[i] == splice[i+1] and i != len(splice)-2:
                repTime += 1
            elif splice[i] == splice[i+1] and i == len(splice)-2:
                repTime += 1
                final.append(repTime)
                final.append((splice[i]))
                repTime = 1
            else:
                if repTime == 1:
                    final.append(splice[i])
                    if i == len(splice)-2:
                        final.append(splice[i+1])
                else:
                    final.append(repTime)
                    final.append(splice[i])
                    if i == len(splice)-2:
                        final.append(splice[i+1])
                    repTime = 1

        temp = ""
        for lst in final:
            temp += str(lst)
        if answer > len(temp):
            answer = len(temp)

        final = []

    if len(s) == 1:
        answer = 1

    return answer

# s = "xxxxxxxxxxyyy"
# s = "xababcdcdababcdcd"
# print(solution(s))