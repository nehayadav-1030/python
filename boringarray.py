n=int(input())
l=list(map(int,input().split()))
l.sort()
l.j=0,len(l)-1
res=0
while i<j:
    res+=abs(l[i]-l[j])
    i+=1
    j-=1
print(res)