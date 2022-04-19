def sum_in_list(search_sum, sorted_list):
    for i in range(0, len(sorted_list)):
        for j in range(i, len(sorted_list)):
            if search_sum == sorted_list[i] + sorted_list[j]:
                return True
    
    return False


print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))