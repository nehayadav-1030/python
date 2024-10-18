l=list(map(int,input().split()))
d,mx=0,0
for i in l:
    d+=i
    if abs(d)>mx:
           mx=abs(d)
    print(mx)