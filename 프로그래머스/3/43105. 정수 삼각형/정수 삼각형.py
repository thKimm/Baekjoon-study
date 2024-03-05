'''
point
1. bottom up방식
    밑에 애들 중 최대값을 자기 자신과 더해서 저장
'''
def solution(triangle):
    result = [[0]*n for n in range(len(triangle),0,-1)]
    for n in range(len(triangle),0,-1):
        if n == len(triangle):
            result[len(triangle)-n] = triangle[n-1]
        else :
            for i in range(n):
                result[len(triangle)-n][i] = triangle[n-1][i] + max(result[len(triangle)-n-1][i],result[len(triangle)-n-1][i+1])
    answer = result[-1][0]
    return answer