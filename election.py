k=int(input())
l=list(map(int,input().split()))
d={ }
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
lis=list(d.items())
lis.sort(reverse=True,key=lambda x:x[1])
if len(lis)==1:
    print(l[0][0])
else:
    if lis[0][1]==lis[1][1]:
        print(-1)
    else:
        print(lis[0][0])