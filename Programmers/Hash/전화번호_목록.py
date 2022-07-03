def solution(phone_book):
    new_lst = []
    for string in phone_book:
        new_lst.append(list(map(int, string)))

    new_lst.sort()

    for i in range(0, len(new_lst)-1):
        if new_lst[i] == new_lst[i+1][0: len(new_lst[i])]:
            return False

    return True
