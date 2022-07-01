from itertools import combinations

def solution(orders, course):
    temp = orders
    orders = []
    for o in temp:
        l = list(o)
        l.sort()
        orders.append(''.join(l))
    answer = []

    for c in course:
        collection = []
        collection2 = []
        count = {}
        for order in orders:
            collection.append(list(combinations(order, c)))
        for i in collection:
            for j in i:
                collection2.append(''.join(j))
        for i in collection2:
            if i not in count.keys():
                count[i] = 1
            else:
                count[i] += 1
        if not count:
            continue
        else:
            maxNo = count[max(count, key=count.get)]
            if maxNo < 2:
                continue
        for c in count.items():
            k, v = c
            if v == maxNo:
                answer.append(k)
        
    answer.sort(key=lambda x:x)
    return answer


# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]
# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]

# print(solution(orders, course))

"""
I have used itertools module to help my code sorted out with combinations.

It would have been hard if i didn't know the existance of combinations module.
"""
