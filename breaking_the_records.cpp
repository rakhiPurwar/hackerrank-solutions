vector<int> breakingRecords(vector<int> scores) {
int i,mins,maxs;
maxs = scores[0],mins = scores[0];
vector<int> result;
result.push_back(0); #for arr[0] we are pushing the value 0 i.e initialising it with 0 for the max record
result.push_back(0); #for the next array element i.e arr[1] we are pushing the value 0 i.e initialising it with 0 for the min record
for(i = 0;i < scores.size();i++)
{
    if(scores[i] > maxs)
    {
        maxs = scores[i];
        result[0]+=1;
    }
   if(scores[i] < mins)
    {
        mins = scores[i];
        result[1]+=1;
    }
}
return result;
}
