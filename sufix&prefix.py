n=int(input())
l=list(map(int,input().split()))
right=sum(l)
res=[]
left=0
for i in range(n):
    left+=l[i]
    right-=l[i]
    res.append(abs(right-left))
print(res)