def find_same_number(some_list):
    elements_seen_so_far = {}
    for number in some_list:
        if number not in elements_seen_so_far.keys():
            elements_seen_so_far[number] = True
        else:
            return number
    

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

"""
DP_Memoization, O(n)
"""

## Below method is using bruteforcing ##

# def find_same_number(some_list):
#     for i in range(0, len(some_list)):
#         for j in range(i+1, len(some_list)):
#             if some_list[i] == some_list[j]:
#                 return some_list[i]
    

# # 중복되는 수 ‘하나’만 리턴합니다.
# print(find_same_number([1, 4, 3, 5, 3, 2]))
# print(find_same_number([4, 1, 5, 2, 3, 5]))
# print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

# Bruteforcing: O(n^2)