import math

def solution(clothes):
    hash_table = {}
    answer = 1
    for cloth in clothes:
        if cloth[1] not in hash_table.keys():
            hash_table[cloth[1]] = 1
        else:
            hash_table[cloth[1]] += 1

    for key in hash_table.keys():
        answer *= (math.factorial(hash_table[key])/math.factorial(hash_table[key]-1) + 1)
    
    answer -= 1
    return int(answer)

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))