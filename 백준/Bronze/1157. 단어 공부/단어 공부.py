alphabet = {chr(s) : 0 for s in range(ord("a"),ord("z")+1)} 
import sys
#S = sys.stdin.readline()
S = input().lower()
for i in range(len(S)):
        alphabet[S[i]] += 1
    
nums = [alphabet[s] for s in alphabet]

Max = max(nums)

cnt = nums.count(Max)

if cnt == 1:
    print(list(alphabet)[nums.index(Max)].upper())
else:
    print("?")