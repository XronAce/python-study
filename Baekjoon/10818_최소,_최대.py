N = int(input())

numstr = input()
numlist = list(map(int, numstr.split()))

answer = ''
answer += str(min(numlist))
answer += ' ' + str(max(numlist))

print(answer)