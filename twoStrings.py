def twoStrings(s1, s2):
    for i in range(0,len(s1)):
        if s1[i] in s2:
            return "YES"
    return "NO"
