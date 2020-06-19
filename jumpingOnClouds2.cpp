int jumpingOnClouds(vector<int> c, int k) {
    int i = 0,energy=99;
    int n = c.size();
    i=k%n;
    if(c[i] == 1)
      energy-=2;

    while(i!=0)
    { 
        energy-=1;
        if(c[(i+k)%n] == 1)
        {
            energy-=2;
        }
        cout<<energy;
        i+=k;
        cout<<i;
        i%=n;
    }
    
    return energy;


}
