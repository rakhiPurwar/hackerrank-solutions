int theLoveLetterMystery(string s) {
    int i,c = 0;
    int p = s.size();
    for(i=0;i<p/2;i++)
    {
        if(s[i]!=s[p-1-i])
        {   
            if(s[i]>s[p-1-i])
             c+=abs(s[i]-s[p-1-i]);
            else 
             c+=abs(s[i]-s[p-1-i]);
        }
    }
     return c;

}
