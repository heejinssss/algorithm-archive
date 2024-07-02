import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K: # heap의 첫번째 인덱스가 가리키는 값은 "최솟값"
        if len(scoville) == 1:
            return -1

        minA = heapq.heappop(scoville)
        minB = heapq.heappop(scoville)
        
        minC = minA + minB * 2
        heapq.heappush(scoville, minC)
        answer += 1

    return answer