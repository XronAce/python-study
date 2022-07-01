import heapq

def solution(scoville, K):
    isAllOverK = 0
    answer = 0
    heapq.heapify(scoville)
    while isAllOverK == 0:
        if scoville[0] < K:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + b * 2)
            answer += 1
        for i in range(len(scoville)):
            if scoville[i] < K:
                isAllOverK = 0
                break;
            else:
                isAllOverK = 1
        if len(scoville) == 1:
            if scoville[0] < K:
                answer = -1
                isAllOverK = 1
    
    return answer

"""
heapq module: binary tree 기반의 min heap 자료구조를 제공함.
heapify(): 기존의 리스트를 heap으로 변환
heappop(heap): 가장 작은 원소를 삭제 후 그 값을 리턴
heappush(heap, element): element를 heap에 추가
"""