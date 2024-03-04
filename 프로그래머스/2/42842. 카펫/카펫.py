'''
point
1. brown + yellow의 제곱근크기만큼 세로를 늘리면 됨
2. 그리고 하나씩 늘려가면서 탐색
'''
def solution(brown, yellow):
    area = brown+yellow
    answer=[]
    for hor in range(2,int(area**0.5)+1):
        if area%hor != 0: continue
        ver = area//hor
        yellows = (hor-2)*(ver-2)
        browns = area - yellows
        if browns == brown and yellows == yellow:
            answer = [max(ver,hor),min(ver,hor)]
    return answer