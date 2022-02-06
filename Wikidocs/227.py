def print_mxn(string, m):
    cnt = 0
    for i in string:
        print(i, end="")
        cnt += 1
        if cnt % m == 0:
            print()

print_mxn("아이엠어보이유알어걸", 3)