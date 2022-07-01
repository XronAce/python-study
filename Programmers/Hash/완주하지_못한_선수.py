def solution(participant, completion):
    answer = ''
    hash_table = {}
    for name in participant:
        if name in hash_table.keys():
            hash_table[name] += 1
        else:
            hash_table[name] = 1
    
    for name in completion:
        hash_table[name] -= 1
    
    for key in hash_table.keys():
        if hash_table[key] > 0:
            answer = key
    
    return answer