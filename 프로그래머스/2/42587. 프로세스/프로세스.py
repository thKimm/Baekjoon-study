'''
Point
1. q.append((prior,loc))
2. 최대힙
'''
def solution(priorities, location):
    answer = 0
    import heapq
    task = [(priorities[i],i) for i in range(len(priorities))]
    cnt = 0
    while 1:
        Max = max(task, key=lambda x:x[0])
        p,i = task.pop(0)
        if p < Max[0]:
            task.append((p,i))
            continue
        else :
            cnt += 1
        if i == location:
            answer = cnt
            break
        
    
    return answer