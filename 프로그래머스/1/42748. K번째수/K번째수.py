'''
point
1. 연산량 많지 않음 -> 슬라이싱
2. 왜 정렬이지?
    정렬 자체의 복잡도 -> O(nlogn) 많지 않음
'''
def solution(array, commands):
    answer = []
    for c in commands:
        i,j,k = c
        answer.append(sorted(array[i-1:j])[k-1])
    return answer