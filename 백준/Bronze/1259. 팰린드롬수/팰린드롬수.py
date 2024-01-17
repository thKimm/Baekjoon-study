S = input().strip()
ans=list()
while S != "0":
    It = len(S)//2
    chk = [S[i] == S[-i-1] for i in range(int(It))]
    if False in chk:
        ans.append("no")
    else: ans.append("yes")
    S=input().strip()
for ANS in ans:
    print(ANS)