'''
예전에 풀었던 문제
point
1. min, max heap
2. nums를 둬서 절댓값의 -값 카운트
3. chk는 원래 큐 개수 카운트
'''

def solution(operations):
    from heapq import heapify, heappop,heappush 
    answer = []
    minh = []
    maxh = []
    nums = dict()
    chk = 0
    for o in operations:
        S,n = o.split()
        n = int(n)
        if S == 'I':
            heappush(minh,n)
            heappush(maxh,-n)
            try:
                nums[n] += 1
            except:
                nums[n] = 1
            chk += 1
        else :
            if chk < 1:
                pass
            else:
                if n == -1:
                    Min = heappop(minh)
                    while nums[Min] == 0: # 남아있는 개수 체크. 안남아있는애라면 남아있을 때까지 계속 뽑기
                        Min = heappop(minh)
                    nums[Min] -= 1
                else :
                    Max = heappop(maxh)
                    while nums[-Max] == 0:
                        Max = heappop(maxh)
                    nums[-Max] -= 1
                chk -= 1
    if chk == 0:
        answer = [0,0]
    else :
        q_max = [-i for i in maxh if nums[-i] > 0]
        q = list(set(minh)&set(q_max))
        answer = [max(q),min(q)]
    return answer