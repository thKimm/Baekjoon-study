'''
point
1. 가장 낮은 지점부터 시작해서 1씩 올림
    -30000 -29999 이렇게
2. 그리고 겹치는 갯수 조사
    늘어나거나 가만히 있으면 계속 올림
    줄어들면 멈춤
    겹치는 애들 삭제
    다시 그 다음부터 조사
=> 답은 맞는데, route가 많아질수록 증가
'''
def solution(routes):
#     roads = {i:0 for i in range(-30000,30001)}
#     visited = [False]*len(routes)
#     for r in routes:
#         for i in range(r[0],r[1]+1):
#             roads[i] += 1
    
#     start = -30000
#     pre = 0
#     answer = 0
#     while start <= 30000:
#         if roads[start] - pre < 0 : # 줄어들면
#             for i in range(len(routes)):
#                 if not visited[i]:
#                     if routes[i][0] <= start <= routes[i][1]: # 경로 안에 있다면
#                         visited[i] = True
#                         for j in range(routes[i][0],routes[i][1]+1):
#                             roads[j] -= 1
#             answer += 1
#         pre = roads[start]
#         start += 1
    ### 같은 아이디어지만 훨씬 간단
    answer = 0
    routes.sort(key=lambda x:(x[1], x[0])) # 끝점이 작은 애부터 정렬. 왜냐면 결국 끝점에 걸리느냐 마느냐로 계속 세니까
    i = 0
    while i < len(routes):
        pos = routes[i][1] # 현재 조사보다 이전 시점의 끝점 : 현재 조사보다 끝점이 낮은 애
        i += 1
        while i < len(routes) and routes[i][0] <= pos <= routes[i][1]: # 그 pos가 현재 routes를 포함한다면 i += 1
            i += 1
        answer += 1
    
    return answer