N = int(input())
nums = input()
count = 0

numList = list(map(int, nums.split()))

for i in numList:
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                count += 1
            break

print(count)