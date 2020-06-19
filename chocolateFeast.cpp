int chocolateFeast(int n, int c, int m) {
    int p,w,ch;
    p = n/c;
    ch = n/c;
    w = ch;
    while(w/m > 0)
    {
        ch = w/m;
        w = w % m;
        p+=ch;
        w=w+ch;
    }
    return p;
}
