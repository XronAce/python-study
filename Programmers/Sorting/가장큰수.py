def solution(numbers):
    stringlist = []
    for number in numbers:
        stringlist.append(str(number))
    stringlist.sort(key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(stringlist)))
    return answer

# print(solution([6, 10, 2]))

