def min_fee(pages_to_print):
    pages_to_print = sorted(pages_to_print)
    i = 1
    fee = 0

    while i < len(pages_to_print)+1:
        for j in range(0, i):
            fee += pages_to_print[j]
        i += 1

    return fee

# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
