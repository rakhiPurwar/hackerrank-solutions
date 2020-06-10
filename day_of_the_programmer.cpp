string dayOfProgrammer(int year) {
     int d;
     if(year >= 1700 && year<=1917)
     {
         d=year%4==0?12:13;
     }
     else if(year >= 1919 && year<=2700)
     {
         d = (year%400 ==0 || (year % 4 == 0 && year%100!=0))?12:13;
     }
     else
     {
         d=26;
     }
     return to_string(d)+".09."+to_string(year);
}
