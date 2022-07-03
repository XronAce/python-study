def solution(phone_book):
    new_lst = []
    for string in phone_book:
        new_lst.append(list(map(int, string)))
    
    new_lst.sort(key = lambda x: len(x))

    for i in range(0, len(new_lst)):
        for j in range(i+1, len(new_lst)):
            if new_lst[i] == new_lst[j][0: len(new_lst[i])]:
                return False

    return True

