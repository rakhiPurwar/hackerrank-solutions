int viralAdvertising(int n) {
int i=1,c=1,s=0,p=5;
while(i<=n)
{
    s+=p/2;
    c=p/2;
    p=c*3;
    i+=1;
    cout<<s;
}
return s;
}
