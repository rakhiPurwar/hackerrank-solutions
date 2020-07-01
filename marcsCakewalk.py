def marcsCakewalk(calorie):
    s = 0
    calorie.sort(reverse = True)
    for i in range(0,len(calorie)):
        s+=(2**i)*calorie[i]
    return s
