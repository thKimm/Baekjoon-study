'''
Point
1. q pop
2. 날짜 기억해뒀다가 넘어가면 q pop 되면 곱해서 100 넘으면 넣어주기
'''

def solution(progresses, speeds):
    from collections import deque
    q = deque()
    answer = []
    full = 0
    for _ in range(len(speeds)):
        q.append((progresses.pop(0),speeds.pop(0)))
    days = 0
    pro, speed = q.popleft()
    while q:
        days += (100-pro-speed*days)//speed if (100-pro-speed*days)%speed == 0 else (100-pro-speed*days)//speed + 1
        while pro + speed*days >= 100:
            full += 1
            if q:
                pro,speed = q.popleft()
            else : break
        answer.append(full)
        full = 0
    if pro + speed*days < 100:
        answer.append(full+1)
    return answer