'''
point
1. BFS로, 간선은 바로 다음 애로 넘어가는 걸로
2. 다음 노드, 현재 값을 모두 q에 넣어주기
'''

def solution(numbers, target):
    answer = 0
    graph = [[i] for i in range(1,len(numbers))] + [[]]
    from collections import deque
    q = deque()
    q.append((0,numbers[0]))
    q.append((0,-numbers[0]))
    result = []
    while q:
        v,now = q.popleft()
        if not v == len(numbers) -1:
            for i in graph[v]:
                q.append((i,now+numbers[i]))
                q.append((i,now-numbers[i]))
        else:
            result.append(now)
    answer = len(list(filter(lambda x:x==target,result)))   
    return answer