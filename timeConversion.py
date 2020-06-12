def timeConversion(s):
    #
    # Write your code here.
    #
    p=s.split(':')
    print(p)
    if(p[0]=='12'):
        p[0]="00"
    if(p[2][2] == "P"):
         p[0]=str(12+int(p[0]))
    result=(':').join(p)
    return result[:-2]
