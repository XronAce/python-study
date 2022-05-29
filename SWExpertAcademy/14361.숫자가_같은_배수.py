from itertools import permutations

T = int(input())

for test_case in range(1, T+1):
    num = input()
    numlist = list(num)
    nPr = list(permutations(numlist, len(numlist)))
    answer = 'impossible'

    for i in range(0, len(nPr)):
        newnum = ''.join(nPr[i])
        if newnum[0] == '0':
            continue
        if newnum == num:
            continue
        if int(newnum) % int(num) == 0:
            answer = 'possible'

    print(f"#{test_case} {answer}")
