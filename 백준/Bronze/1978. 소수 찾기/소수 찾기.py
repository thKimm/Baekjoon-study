def is_prime(num):
    if num== 1:
        return False
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True
        
n_nums = int(input())
nums = list(map(int,input().split()))

n_prime = [is_prime(num) for num in nums]
print(n_prime.count(True))