def solution(new_id):
    #1단계
    new_id = new_id.lower()

    #2단계
    lst = list(new_id)
    for i in range(0, len(lst)):
        if not lst[i].isalpha():
            if not lst[i].isdigit():
                if lst[i] not in ['-', '_', '.']:
                    lst[i] = ''
    new_id = ''.join(lst)

    #3단계
    lst = list(new_id)
    flag = 0
    for i in range(0, len(lst)-1):
        if lst[i] == '.':
            if lst[i] == lst[i+1]:
                lst[i] = ''
    new_id = ''.join(lst)

    #4단계
    new_id = new_id.strip('.')

    #5단계
    if new_id == '':
        new_id = 'a'

    #6단계
    lst = list(new_id)
    while len(lst) >= 16:
        lst.pop()
    new_id = ''.join(lst)
    new_id = new_id.strip('.')

    #7단계
    lst = list(new_id)
    while len(lst) <= 2:
        lst.append(lst[len(lst)-1])
    new_id = ''.join(lst)

    answer = new_id

    return answer

# new_id = "...!@BaT#*..y.abcdefghijklm"
# new_id = "=.="
# print(solution(new_id))