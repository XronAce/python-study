def solution(genres, plays):
    answer = []
    genre_playNum = {}
    for i in range(len(genres)):
        if genres[i] not in genre_playNum.keys():
            genre_playNum[genres[i]] = plays[i]
        else:
            genre_playNum[genres[i]] += plays[i]
    
    sorted_genre_playNum = sorted(genre_playNum.items(), key = lambda item: item[1], reverse=True)

    hash_table = {}
    for i in range(0, len(genres)):
        if genres[i] not in hash_table.keys():
            hash_table[genres[i]] = [(plays[i], i)]
        else:
            hash_table[genres[i]].append((plays[i], i))
    

    for i in range(0, len(hash_table)):
        hash_table[sorted_genre_playNum[i][0]].sort(key = lambda x: x[0], reverse=True)
    
    for i in range(0, len(hash_table)):
        if len(hash_table[sorted_genre_playNum[i][0]]) == 1:
            answer.append(hash_table[sorted_genre_playNum[i][0]][0][1])
        else:
            answer.append(hash_table[sorted_genre_playNum[i][0]][0][1])
            answer.append(hash_table[sorted_genre_playNum[i][0]][1][1])

    return answer

# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]
# print(solution(genres, plays))

"""
hash_table format:
{'genre name': [(playNum, i)]}
hash_table has been sorted to have its playNum in descending order.
sorted_genre_playNum is created to have genre name sorted with its total playNum in descending order.

A bit scratchy tho.
"""