from collections import Counter

# Complete the anagram function below.
def anagram(s):
    c = 0
    l = len(s)
    r = int(l/2)
    print(r)
    print(l)
    if l%2 != 0:
        return -1
    else:
        p = Counter(s[0:r])
        q = Counter(s[r:l])
        diff = p - q
        print(diff)
        return sum([val for key,val in diff.items()])
