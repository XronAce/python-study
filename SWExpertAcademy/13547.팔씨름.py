T = int(input())

for test_case in range(1, T+1):
    string = input()
    oxList = []
    for i in range(0, len(string)):
        oxList.append(string[i])
    cnto = 0

    for i in range(0, len(oxList)):
        if oxList[i] == 'o':
            cnto += 1

    #남은 판수
    leftover = 15 - len(oxList)

    #남은 승수
    leftwin = 8 - cnto

    if leftover >= leftwin:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")