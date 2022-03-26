def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    if i < len(list1):
        merged_list += list1[i:]
    elif j < len(list2):
        merged_list += list2[j:]
        

    return merged_list
    
    
# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))

"""
Given list1 and list2 are sorted lists, so there's no need to sort.

No need to sort... why is this a merge 'sort'..?

Regardless of sorting, need to apply with 'divide and conquer' paradigm.

---------------
NVM this merge function does not need divide and conquer paradigm.
"""