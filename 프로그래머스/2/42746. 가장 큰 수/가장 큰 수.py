'''
point
1. 앞자리마다 모으고 -> 1번 케이스 해결
2. 걔네마다 sort. 
    뒷자리가 크다면? 그리고 하나하나 다 하려면 시간이 너무 오래걸림. 경우의 수가 1000!
    3 34 30이 있으면 sort.reverse하면 34 30 3 근데 이거보다 34 3 30이 더 큼 sort.reverse,x%10하면 34 3 30
    343 34 3이 있으면 sort.reverse 343 34 3, %10 343 34 3, 34 343 3이 더 큼. %10 if 100보다 작으면 아니면 %100//10 
    
공부 
    343 34 3이 있으면 sort.reverse 343 34 3, %10 343 34 3, 34 343 3이 더 큼. %10 if 100보다 작으면 아니면 %100//10 
    343 이랑 34를 비교할 땐 343 34랑 34 343 중 누가 더 큰지 비교하게 됨
    343 이랑 3을 비교할 땐 3 343이랑 343 3이랑 누가 더 큰지 비교하게 됨
    즉, 자리수가 더 큰애가 있으면, 작은애가 가지지 못한 다음 값을 본인과 비교하면 됨.
    이때, 4자리 수까지 있을 수 있으니 str(x)*4로 비교하면 끝임
    
'''
def solution(numbers):
    answer = ''
    nums = list(map(str,numbers))
    answer += str(int("".join(sorted(nums,key=lambda x:x*4,reverse=True))))
    return answer