def countingValleys(n, s):
    v = 0
    l = 0
    for i in s:
        if i == 'U':
            l+=+1
        if i == 'D':
            l+=-1
        if l == 0 and i == 'U':
            v+=1
    return v
    
    
    
    logic:
    when it is a downhill we need to decrment the level by 1
    and when it's uphill we need to increment it by 
    when the level is 0 and the i is uphill, means a valley is created otherwsise not.
