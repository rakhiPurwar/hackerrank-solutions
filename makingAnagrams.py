def makingAnagrams(s1, s2):
    p = Counter(s1)
    q = Counter(s2)
    ans = 0
    for key in p.keys():
        if key in q.keys():
            ans+=min(p.get(key),q.get(key))
    return len(s1)+len(s2)-2*ans
