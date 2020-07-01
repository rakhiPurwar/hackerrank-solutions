def counterGame(r):
    p = 1
    if r == 1:
        return "Louis"
    else:
        while r>1:
            p+=1
            if r & r-1 == 0:
                r=r>>1
            else:
                q = 1
                while q <= r:
                    q<<= 1
                q = q>>1
                r=r-q
    if p%2 == 0:
        return "Louise"
    else:
        return "Richard"

