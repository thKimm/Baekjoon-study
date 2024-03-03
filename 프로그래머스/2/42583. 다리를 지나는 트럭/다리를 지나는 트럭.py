"""
point
1. FIFO 큐
2. 다리를 올라오는애를 큐에 stack
3. cnt가 다 되면 pop
"""
def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 1
    from collections import deque
    q = deque()
    w = truck_weights[0]
    q.append((truck_weights.pop(0),1))
    while q:
        time += 1
        for _ in range(len(q)):
            truck,t = q.popleft()
            if t + 1 > bridge_length:
                w -= truck
                continue
            q.append((truck,t+1))
        if len(truck_weights) > 0:
            if w+truck_weights[0]<= weight :
                w += truck_weights[0]
                q.append((truck_weights.pop(0),1))
    return time