
#include <iostream>
using namespace std;

int main()
{
    int T,N,x=0,arrSum=0,count=0;
    cin>>T;
    for(int i=0;i<T;i++){
        cin>>N;
        int *arr = new int[N];
        int *arrCheck = new int[N];
        
        for(int j;j<N;j++){
            cin>>arr[j];
            arrCheck[j]=0;
        }
        arrCheck[0]=1;
        while(arrCheck[N-1]!=1){
            while(1){
                if(arrCheck[x]==0){
                    break;
                }
                else{
                    arrSum=arrSum+arr[x];
                    x=x+1;
                }
            }
            for(int y=1;y<arrSum+1;y++){
                arrCheck[y]=1;
            }
            count=count+1;
        }
        cout<<count<<endl;
    }
}
