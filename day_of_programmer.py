def dayOfProgrammer(year):
    if year in range(1700,1918):
        if year%4==0:
            d=12
        else:
            d=13
    elif year in range(1919,2701):
        if (year%4==0 and year%100!=0) or (year%400 == 0):
            d = 12
        else:
            d=13
    else:
        d=26
    
    return str(d)+".09."+str(year)
