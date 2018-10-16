T=int(input())
for i in range (0,T):
    N=int(input())
    tempSum=0
    arrSum=0
    x=0
    count=0
    arr=[]
    arrcheck=[]
    arr=input().split(' ')
    for j in range(0,N):
        arr[j]=int(arr[j])
        arrcheck.append(0)
    arrcheck[0]=1
    while(arrcheck[N-1]!=1):
        tempSum=arrSum
        while(arrcheck[x]!=0):
            arrSum=arrSum+arr[x]
            x=x+1
        arrSum=tempSum+arrSum    
        for y in range (tempSum,arrSum+1):
            if(y<N):
                arrcheck[y]=1
            else:
                break    
        count=count+1    
    if(count==0):
        count=1
    print(count)                