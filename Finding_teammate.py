t = int(input())
for i in range(t):
    n = int(input())
    li = input().split()
    li = [int(j) for j in li]
    pr = 1
    c = 0
    while li != []:
        maxm = max(li)
        ind = li.index('maxm')
        li.remove(ind)
        maxn = max(li)
        c1 = count(maxn)
        if c1>1:
            pr = pr*c1
        li.remove(maxn)
        c = c+1
    c = c*pr
    print(c)
        
