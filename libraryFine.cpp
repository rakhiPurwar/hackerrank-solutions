int libraryFine(int d1, int m1, int y1, int d2, int m2, int y2) {
    int fine = 0;
    if((m1 == m2) && (y1 == y2) && d1>d2)
    {
        fine+=(d1-d2)*15;
    }
    else if( m1>m2 && y1==y2)
    {
        fine+=(m1-m2)*500;
    }
    else if(y1>y2)
    {
        fine+=10000;
    }
 
 return fine;


}
