'''
point
1. -가 나오면 뒤에 있는 애들을 싹 괄호로 묶어주면 됨

풀이
point1. tail의 min, max를 계속 트래킹 해주면 됨
    -를 만났을 때
    다음 -를 만나기 전까지 a + b + c + d + tail라면 
        - a+b+c+d의 최대값은 다 sum, 즉 제일 많이 빼지는, 결과가 min으로 나오는 애는 -sum(a+b+c+d) = min_sub
        - a+b+c+d의 애들의 최소값은 하나면 -, 즉 제일 적게 빼지는, 결과가 max으로 나오는 애는 -a+b+c+d = max_sub
    그럼 a + b + c + d + tail 의
        최대값은 max_sub+tail_max min_sub-tail_min
        최소값은 min_sub+tail_min min_sub-tail_max
'''
def solution(arr):
    arr = ''.join(arr).split('-') ### ['5+1', '3+1+2', '1', '4+2']
    a0 = sum([*map(int, arr[0].split('+'))]) ### 6 (초항 합계)

    min_tail, max_tail = 0, 0    
    for a in arr[:0:-1]: ### ['4+2', '1', '3+1+2'] 초항 제외 역순
        sub = [*map(int, a.split('+'))] ### [4,2] --> [1] --> [3,1,2]
        min_sub = -sum(sub)             ###  -6,  --> -1  --> -6 (전체 음수인 합계)
        max_sub = -2*sub[0] -min_sub    ###  -2,  --> -1  -->  0 (첫항만 음수인 합계)
        max_tail, min_tail = max(max_sub +max_tail, min_sub -min_tail), min(min_sub +min_tail, min_sub -max_tail)
    return a0 +max_tail

