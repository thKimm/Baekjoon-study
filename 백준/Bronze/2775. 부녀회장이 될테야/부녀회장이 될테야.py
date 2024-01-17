n_nums = int(input())
for i in range(n_nums):
    K = int(input())
    N = int(input())
    under = [i+1 for i in range(N)]
    for k in range(K-1):
        Sum = 0
        for n in range(N):
            Sum += under[n]
            under[n] = Sum
            
    print(sum(under))