int minimumDistances(vector<int> a) {
    int i,j, p = 0,min =-1;
    vector<int> b;
    for(i=0;i<a.size()-1;i++)
    {
        for(j =i+1 ; j<a.size();j++)
           {
            if(a[i]==a[j])
                {
                    b.push_back(j-i);
                }
           }
    }
    if(b.size()>0)
    {
      p = *min_element(b.begin(),b.end());
      
        if(p>min)
        {
            return p;
        }
    }
    return min;  }
