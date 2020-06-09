int divisibleSumPairs(int n, int k, vector<int> ar) {
int count=0,i,j;
for(i=0;i<ar.size();i++)
{
    for(j=i+1;j<ar.size();j++)
    {
        if((ar[i]+ar[j]) % k == 0)
        {   
            count+=1;
        }
        else
        {
            count+=0;
        }
    }
}
return count;
}
