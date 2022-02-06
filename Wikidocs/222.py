def print_score(lst):
    avg = 0
    for i in lst:
        avg += i
    print(avg/len(lst))

print_score([1,2,3])