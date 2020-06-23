vector<string> split_string(string);

// Complete the pairs function below.
int pairs(int k, vector<int> arr) {
    int c=0,i=0,j=1,n;
    n = arr.size();
    sort(arr.begin(),arr.end()); 
    while(i<n && j<n)
    {
        if(i!=j && arr[j]-arr[i]==k)
        {
            c+=1;
            i++;
        }
        else if(arr[j]-arr[i]<k)
        {
            j++;
        }
        else
            i++;
    }
    return c;

}
