def sumXor(n):
    c = 0
    while n:
        if n%2 == 0:
            c+=1
        n = n//2
    return 2**c
