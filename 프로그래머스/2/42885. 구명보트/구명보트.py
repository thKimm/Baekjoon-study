'''
point
1. sort
2. 무게 제한 넘지 않는 만큼 2개 최대한 크게 묶기
    제일 무게가 많이 나가는 조합부터 묶기
        제일 큰애 + 제일 작은애 vs 제일 큰애 + 남은 것 중 제일 작은 애 계속 비교 
        until 제일 큰애 + 남은 것 중 제일 작은 애 > limit
'''
def solution(people, limit):
    people.sort()    
    cnt = 0
    # result = []
    # while len(people)>0:
    #     now = people.pop()
    #     remain = limit - now
    #     small = -1
    #     for i in range(len(people)):
    #         if people[i] <= remain:
    #             small = i
    #     if small != -1:
    #         result.append([now,people.pop(i)])
    #     else:
    #         result.append([now])
    # if len(people)==1:
    #     result.append(people.pop())
    ### 동일 아이디어이지만, 투포인터로 더 간단한 풀이
    front, end = 0,len(people)-1
    
    while front <= end:
        if people[front] + people[end] <= limit: # 두명 태울 수 있으므로 front 찾는걸 하나 증가
            front += 1
        end -= 1 #탐색 완료니까 end 줄임
        cnt += 1
        
    return cnt
