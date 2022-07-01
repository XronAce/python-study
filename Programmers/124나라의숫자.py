def solution(n):
    nlist = []
    if n == 1:
        answer = '1'
    elif n == 2:
        answer = '2'
    elif n == 3:
        answer = '4'
    else:
        while n > 3:
            q = n // 3
            r = n % 3
            if r == 0:
                nlist.insert(0, 4)
                q -= 1
            else:
                nlist.insert(0, r)
            n = q
            if n == 1:
                nlist.insert(0, 1)
            elif n == 2:
                nlist.insert(0, 2)
            elif n == 3:
                nlist.insert(0, 4)
            else:
                pass
        answer = ''.join(str(e) for e in nlist)

    return answer

# print(solution(5))