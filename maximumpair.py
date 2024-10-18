n=int(input())
l=list(map(int,input().split()))
mx=0
res=[-1,-1]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j] and l[i]+l[j]==18:
            prod=l[i]*l[j]
            if prod>mx:
                mx=prod
                res[0],res[1]=l[i],l[j]
print(res)