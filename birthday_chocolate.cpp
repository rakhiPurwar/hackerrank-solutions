int birthday(vector<int> s, int d, int m) {
    int sum=0,i,end,count=0;
    for(i=0;i<m;i++)
    {
        sum += s[i];
    }
    if(sum== d)
        count+=1;
    cout<<sum;
    for(end=m;end<s.size();end++)
    {
        sum = sum + s[end] - s[end-m];
        cout<<sum;
        if(sum == d)
          count+=1;
        else
           count+=0;
        
    }
    return count;


}
