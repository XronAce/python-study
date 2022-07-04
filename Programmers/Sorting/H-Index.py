def solution(citations):
    maxH = 0
    for h in range(1, len(citations)+1):
        cntOver = 0
        for i in range(0, len(citations)):
            if citations[i] >= h:
                cntOver += 1
        if cntOver >= h:
            maxH = max(maxH, h)

    answer = maxH
    return answer

citations = [3, 0, 6, 1, 5]
print(solution(citations))

"""
Why is this problem in a sorting category..?
H-index definition should be clarified...
"""