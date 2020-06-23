def gameOfThrones(s):
   c = Counter(s)
   print(c)
   p = sum([val%2 for val in c.values()])
   if p <= 1:
    return "YES"
   else:
    return "NO"
   
