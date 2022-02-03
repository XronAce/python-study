리스트 = ['hello.py', 'ex01.py', 'intro.hwp']

for i in 리스트:
    name, _ = i.split(".")
    print(name)