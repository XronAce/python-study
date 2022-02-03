리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in 리스트:
    name, end = i.split(".")
    if end == "h" or end == "c":
        print(i)