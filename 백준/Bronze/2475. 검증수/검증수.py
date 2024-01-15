S = list(map(int,input().split()))
Sum = 0
for i in range(5):
    Sum += S[i]*S[i]
print(f"{Sum%10}")