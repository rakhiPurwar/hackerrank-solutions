def findDigits(n):
    arr = []
    x = n
    c=0
    i = 0
    while  n != 0:
      arr = n%10
      n =n// 10
      arr+=1
    print(arr)
    arr.delete(0)
    for j in range(arr):
        if j == 0:
            c+=0
        if x%j == 0 :
            c+=1
    return c
