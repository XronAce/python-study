N = int(input())
letter = []

for i in range(0, N):
    letter.append(input())

letter = list(set(letter))
letter.sort()

letter.sort(key=lambda x:len(x))

for l in letter:
    print(l)