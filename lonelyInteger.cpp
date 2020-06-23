int lonelyinteger(vector<int> a) {
    int i = 0, res = 0;
    for(i = 0;i<a.size();i++)
    {
        res=res^a[i];
    }
    return res;
}
