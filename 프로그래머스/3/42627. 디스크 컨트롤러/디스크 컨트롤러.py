'''
고민점
1. min heap
    소요시간이 제일 짧은 애를 기준으로 넣기
2. 만약에 긴 애의 요청시간 + 소요시간 < 짧은 애의 요청시간?
    긴 애 부터. 근데, 이때 또 똑같은 문제가 발생할 경우의 수 존재
3. 겹치는 애만 min heap
    뒤로 쭉 나열했을 때 또 겹치면?
point
1. 시간 순서대로 실행
2. 만약 실행 중에 다른 애가 들어오면 대기열에 push
3. 대기열은 min heap
heap 구조
(소요시간, 시작시간, 인덱스)
'''
def solution(jobs):
    answer, i, now  =0,0,0
    l = len(jobs)
    h = []
    import heapq
    while i < l:
        for j in jobs:
            if 0<=j[0]<= now:
                heapq.heappush(h,(j[1], j[0]))
                j[0] = -1
        if h:
            cur = heapq.heappop(h)
            now += cur[0]
            answer += now-cur[1]
            i+=1
        else:
            now +=1

    return answer//l 