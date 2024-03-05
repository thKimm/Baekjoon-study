'''
point
1. 위아래로 움직이는거는 그냥 빼주면
2. 양 옆으로 움직이는건?
    A가 있을 경우 A의 isA
        왼쪽으로 체크
        오른쪽으로 체크
        제일 작은거
        A가 아닌거 chk +1
        ABAAAAAAAAABB <- 이거 못품
    A가 있을 경우 A가 아닌 것 중 가장 가꺄운거
        양방향인데 어떻게?
        alpha*3
        A위치는 저장해놓고 제일 가까운 애를 check
        근데 이렇게 하면 왔다갔다 못함
    절반 나누고, 오른쪽 절반부터 탐색. A가 아닌 첫번째 애를 찾고 걔부터 시작
        6 -> 3
        5 -> 3
        4 -> 2
        3 -> 2
    잘못 생각함. updown은 고정된 값 최적화 할 필요가 없음
    현재 위치에서 원하는 알파벳 도달. 다음 A가 아닌 데까지 이동
    
    포기... 정답 긁어옴
    
'''
def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = float('inf')
    for i in range(len(name) // 2): # 반 이상 움직일 필요 없음 왜? 왼쪽 절반 하면 오른쪽 절반이랑 같음
        left_moved = name[-i:]+name[:-i] # 1234 -> 4 123 i = 1 / 34 12 i = 2
        right_moved = name[i:]+name[:i] # 1234 -> 234 1 i = 1 / 34 12 i = 2
        for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:
            while n and n[-1] == 'A': # 맨 오른쪽 A는 셀 필요 없음. 이미 끝난 애들이니까
                n = n[:-1]

            row_move = i + len(n)-1
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - 65, 91 - c)

            answer = min(answer, row_move + col_move)

    return answer