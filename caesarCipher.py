def caesarCipher(s, k):
    for i in range(0,len(s)):
            if s[i] in range(65,91):
                s[i]=s[i]+k
                if s[i]>90:
                    s[i]=s[i]-26
            if s[i] in range(97,123):
                s[i]=s[i]+k
                if s[i]>122:
                    s[i]=s[i]-26
    return s
