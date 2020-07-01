def appendAndDelete(s, t, k):
    if s==t:
        return "Yes"
    else:
        c = 0  
        for i in range(0,min(len(s),len(t))):
            if s[i]!=t[i]:
                c = i
                break 
            else:
                c=i
        print(c) 
        if len(t)>len(s) and c == len(s) :
            t = t[len(s):]
            s = s[len(s):]
            if  len(t)<=k:
                return "Yes"
            else:
                return "No"
            
        elif (c == len(t)) and len(s)>len(t):
                t = t[len(t):]
                s = s[len(t):]
                if  len(s)<=k:
                    return "Yes"
                else:
                    return "No"

        else:   
            if len(s)+len(t)-2*c<=k:
                return "Yes"
            else:
                return "No"

