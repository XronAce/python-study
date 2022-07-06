def solution(people, limit):
    people.sort()
    boatCnt = 0
    while people:
        if len(people) == 1:
            boatCnt += 1
            people.pop()
        elif people[0] + people[-1] <= limit:
            boatCnt += 1
            people.pop()
            people.pop(0)
        else:
            boatCnt += 1
            people.pop()
    
    answer = boatCnt
    return answer

people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))