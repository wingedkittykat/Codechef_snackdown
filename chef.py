def checkValid(ld,n):
    for i in range(0,n-2):
        while(ld[i]>0):
            ld[i]=ld[i]-1
            ld[i+1]=ld[i+1]-2
            ld[i+2]=ld[i+2]-3
    if(ld[n-1] != 0 or ld[n-2]!=0):
        return False
    else:
        return True     
T=int(input())
for i in range (0,T):
    ld=[]
    N=int(input())
    l1=input().split(' ')
    l2=input().split(' ')
    for j in range (0,N):
        ld.append(int(l2[j])-int(l1[j]))
    if(checkValid(ld,N)):
        print('TAK')
    else:
        print('NIE')        
    
        