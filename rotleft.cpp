vector<int> rotLeft(vector<int> a, int d) {
    vector<int> b;
    int i,start,n;
    n = a.size();
    start = d%n;
    for (int i = start; i <n+start; i++) { 
        b.push_back(a[i%n]); 
    }
    return b;
}
