def fib_tab(n):
    table = {}
    for i in range(1, n+1):
        if i == 1:
            table[i] = 1
        elif i == 2:
            table[i] = 1
        else:
            table[i] = table[i-1] + table[i-2]

    return table[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))