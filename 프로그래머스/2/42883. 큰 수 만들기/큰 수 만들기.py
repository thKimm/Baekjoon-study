'''
point
1. permute로 뺄 수 있는 모든 경우의 수 구하고
2. max값 찾기
=> 시간 초과
풀이
1. stack에 하나씩 넣는데
2. 넣는 애가 stack에 제일 마지막 애(현재 자리 수 중에 제일 작은 애)보다 크면 stack pop
    -> 제일 큰 애부터 넣기 위해 현재 넣는 애가 앞에 보다 크면 앞에 애를 계속 제거
'''
def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    return ''.join(stack[:len(number)-k]) # k가 남으면 뒤에 자르기
