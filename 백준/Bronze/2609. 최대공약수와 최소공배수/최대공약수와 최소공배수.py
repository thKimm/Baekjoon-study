def Factorization(num):
    Com = 2
    num_ = num
    factors=list()
    while num_ != 1:
        if num_%Com==0:
            factors.append(Com)
            num_=num_//Com
        else:
            Com += 1
    Factors = {x:factors.count(x) for x in tuple(factors)}
    return Factors

x,y = list(map(int,input().split()))
x_facts = Factorization(x)
y_facts = Factorization(y)

ComD = 1
ComM = 1

for X in x_facts:
    if X in y_facts:
        ComD *=X**min(x_facts[X],y_facts[X])
        ComM *=X**max(x_facts[X],y_facts[X])
    else :
        ComM *=X**x_facts[X]

for Y in y_facts:
    if Y in x_facts:
        pass
    else:
        ComM *=Y**y_facts[Y]
print(ComD)
print(ComM)
