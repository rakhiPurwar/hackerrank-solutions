def hackerrankInString(s):
    ls = "hackerrank"
    i = 0
    j = 0
    c = 0
    while i<len(ls) and j<len(s):
        if ls[i] == s[j]:
            i+=1
            j+=1
            c+=1
        else:
            j+=1
    if c== len(ls):
        return "YES"
    else:
        return "NO"
