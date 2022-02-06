def print_5xn(string):
    cnt = 0
    for i in string:
        print(i, end="")
        cnt += 1
        if cnt % 5 == 0:
            print()

print_5xn("아이엠어보이유알어걸")