n,m = map(int,input().split())
lis = list(map(int,input().split()))
a = set(map(int,input().split()))
b = set(map(int,input().split()))
hap = 0
for i in range(0,len(lis)):
    if lis[i] in a:
        hap+=1
    if lis[i] in b:
        hap-=1
print(hap)
