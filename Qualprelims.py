t=int(input())
for i in range(0,t):
    n, k = map(int, input().split())
    l=input().split(' ')
    l.sort()
    count=k
    for j in range(k+1,n+1):
        if(int(l[-k])==int(l[-j])):
            count=count+1
        else:
            break
    print(count)        



         