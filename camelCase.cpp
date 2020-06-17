int camelcase(string s) {
int count = 1,i;
for(i = 0; i<s.length();i++)
{
    if(s[i]>=65 && s[i]<=90)
    {
        count+=1;
    }
}
return count;
}
