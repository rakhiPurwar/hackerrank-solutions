def marsExploration(s):
    p = 0
    for i in range(len(s)):
        if s[i]!="SOS"[i%3]:
            p+=1
    return p
