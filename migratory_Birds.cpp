int migratoryBirds(vector<int> arr) {
    int max,index,i,j;
    int c[6]={0};
    for(i=0;i<arr.size();i++)
    {
        c[(arr[i])]+=1;
    }
    max=c[1];
    for(j=1;j<=5;j++)
    {
        if(c[j]>max)
        {   
            index = j;
            max=c[j];
            
        }
    }
    cout<<max;//for debugging
    return index;
}
