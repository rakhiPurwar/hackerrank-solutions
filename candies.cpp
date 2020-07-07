long candies(int n, vector<int> arr) {

  vector<long> vect(n,1);
  long sum =0; 
  int i;
  for(i = 1;i<n;i++)
  {
      if(arr[i]>arr[i-1])
      {
          vect[i]=vect[i-1]+1;
      }
  }
  
   for(int i = n-2 ; i >= 0 ; i--)
   { 
        if(arr[i] > arr[i+1] && vect[i] <= vect[i+1]){
            vect[i] = vect[i+1] + 1;
        }
    }

  for (int i = 0; i < vect.size(); i++) 
        sum+=vect[i] ;
  return sum;

}
