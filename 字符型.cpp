#include<iostream>
using namespace std;

int main(){
    int a,b,c,d,e,f,g,h,i;
    char j;
    char k ='b';//只能用单引号！只能是一个字符！
    scanf("%1d-%1d%1d%1d-%1d%1d%1d%1d%1d-%c",&a,&b,&c,&d,&e,&f,&g,&h,&i,&j);
    int s = a+b+c+d+e+f+g+h+i;
    int s2=s+j;
    cout<<j<<endl;
    cout<<s<<endl;
    cout<<s2<<endl;
    cout<<k<<endl;
    system("Pause");
    return 0;
}
