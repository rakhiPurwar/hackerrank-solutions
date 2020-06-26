def acmTeam(topic):
    print(topic)
    c = 0
    m = 0
    for i in range(0,len(topic)):
        for j in range(i+1,len(topic)):
            p = int(topic[i],2)|int(topic[j],2)
            p = bin(p).replace("0b","")
            n = str(p).count("1")
            if n>=m:
                m=n
                c+=1
    return m,c
