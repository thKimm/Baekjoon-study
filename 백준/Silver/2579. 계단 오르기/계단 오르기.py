import sys

N = int(sys.stdin.readline().strip())
D = [0] * (N+1)
Cont_Step = [0] * (N+1)
Score = [0]
for i in range(N):
    Score.append(int(sys.stdin.readline().strip()))

for i in range(1,N+1):
    if i  == 1:
        D[i] = Score[i]
    elif i == 2:
        D[i] = Score[i-1] + Score[i]
    elif i == 3:
        D[i] = max(Score[i-1] + Score[i],Score[i-2] + Score[i])
    else:
        D[i] = max(D[i-3]+Score[i-1]+Score[i],D[i-2]+Score[i])
    # if step + 1 < 3 an = max(an-1+dn,an-2+dn) else : an = an-2+dn
print(D[N])