T = int(input())
printmsg = ''

for test_case in range(1, T+1):
    time = list(map(int, input().split()))
    A = time[0]
    B = time[1]
    C = time[2]
    D = time[3]


    bothGlowStart = max(A, C)
    bothGlowEnd = min(B, D)

    if bothGlowStart >= bothGlowEnd:
        printmsg += f'#{test_case} 0\n'
       # print(f"#{test_case} 0")
    else:
        printmsg += f'#{test_case} {bothGlowEnd - bothGlowStart}\n'
        #print(f"#{test_case} {bothGlowEnd - bothGlowStart}")

print(printmsg)

"""
Too many testcases causing timeout error due to print function required time.
Saved up the print messages and then printed at once.
"""