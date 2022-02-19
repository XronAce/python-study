N = int(input())
member = []

for i in range(0, N):
    member.append(input())

member.sort(key=lambda x:int(x.split()[0]))

for m in member:
    print(m)