int toys(vector<int> w) {
    int i =0,container = 0;
    sort(w.begin(),w.end());
    int p = w[0];
    for(i=0;i<w.size();i++)
    {
        if(w[i]-p>4)
        {
            p = w[i];
            container+=1;
        }

    }
    return container+1;
}
