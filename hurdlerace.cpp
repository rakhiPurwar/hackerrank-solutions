int hurdleRace(int k, vector<int> height) {
    int max= *max_element(height.begin(), height.end());
    cout<<max;
    if(max>k)
    {
        return max-k;
    }
    else
    {
        return 0;
    }


}
