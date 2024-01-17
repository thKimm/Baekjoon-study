A,B,V = list(map(int,input().split()))
date_ = (V-B)//(A-B)
if (V-B)%(A-B) != 0:
    date_ +=1
print(date_)