def strangeCounter(t):
    rem = 3
    while t>rem:
        t= t -rem
        rem = rem*2
        print(t,rem)

    return rem - t +1
