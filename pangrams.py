def pangrams(s):
    p = set()
    for i in range(0,len(s)):
        if s[i]!=" ":
            p.add(s[i].lower())
    
    if len(p) == 26:
        return "pangram"
    else:
        return "not pangram"
