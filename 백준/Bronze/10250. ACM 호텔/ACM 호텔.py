n_nums = int(input())
fin = []
for i in range(n_nums):
    H,W,N = map(int,input().rstrip().split())    
    O = (N-1) // H + 1
   
    T = N % H 
    if N % H == 0:
        T = H
    fin.append(T*100+O)
for floor in range(n_nums):
    print(fin[floor])