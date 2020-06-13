def maximumToys(prices, k):
    s = 0
    c = 0
    prices.sort()
    for i in range(0,len(prices)):
        s+=prices[i]
        c+=1
        if s>k:
            s=s-prices[i]
            c-=1
            return c
