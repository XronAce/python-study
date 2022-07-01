def solution(lottos, win_nums):
    count = 0
    countZero = 0
    answer = []

    for lotto in lottos:
        if lotto in win_nums:
            count += 1
        elif lotto == 0:
            countZero += 1
    
    if count+countZero == 6:
        answer.append(1)
    elif count+countZero == 5:
        answer.append(2)
    elif count+countZero == 4:
        answer.append(3)
    elif count+countZero == 3:
        answer.append(4)
    elif count+countZero == 2:
        answer.append(5)
    else:
        answer.append(6)

    if count == 6:
        answer.append(1)
    elif count == 5:
        answer.append(2)
    elif count == 4:
        answer.append(3)
    elif count == 3:
        answer.append(4)
    elif count == 2:
        answer.append(5)
    else:
        answer.append(6)

    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))