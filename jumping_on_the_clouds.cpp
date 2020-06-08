int jumpingOnClouds(vector<int> c) {
int i=0,count=0;
while(i<c.size()-1)
{
    if(c[i] == 0)
    {
        if(c[i+1]==0 && c[i+2]==0)
        {
            i+=2;
            count+=1;
        }
        else if(c[i+1]==0 && c[i+2]!=0)
        {
            i+=1;
            count+=1;
        }
        else if(c[i+1]!=0)
        {
            i+=2;
            count+=1;
        }
    }
cout<<count;    
}
return count;

}
