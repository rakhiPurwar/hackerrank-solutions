void bonAppetit(vector<int> bill, int k, int b) {
    int ba=0,sum=0;
    for(int i=0;i<bill.size();i++)
    {
        sum+=bill[i];
        
    }
    ba=sum-bill[k];
    ba=ba/2;
    
    if(ba==b)
    {
        cout<<"Bon Appetit";

    }
    else
    {
        cout<< b-ba;
    }
    }
