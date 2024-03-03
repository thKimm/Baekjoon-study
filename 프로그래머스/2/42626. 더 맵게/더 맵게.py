'''
point
1. min heap
2. 꺼내고, 이게 기준보다 작으면 또 꺼내서 더함
'''
def solution(scoville, K):
    answer = 0
    import heapq
    heapq.heapify(scoville)
    while scoville:
        scov = heapq.heappop(scoville)
        if scov < K:
            if len(scoville) == 0:
                answer = -1
                break
            else :
                heapq.heappush(scoville, scov + 2*heapq.heappop(scoville))
                answer += 1
        
        
    return answer