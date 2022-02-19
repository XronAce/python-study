N = int(input())
num = []

for i in range(0, N):
    num.append(int(input()))

num.sort(key=lambda x:x)

for n in num:
    print(n)