int beautifulDays(int i, int j, int k) {
    int count=0,reverse,n;
    for(int r=i;r<=j;r++)
    {
        reverse=0;
        n=r;
        
        while(n!=0)
        {
        reverse=reverse*10+n % 10;
        n=n/10;
        }
        if(((r-reverse)%k) == 0)
        { 
          count+=1;
        }
   }
    return count;
}  
