n=int(input())
res=0
cur=1000
comma=1
while cur<n:
    next=cur*1000
    nums=min(n-cur+1,next-cur)
    res+=nums*comma
    cur=next
    comma+=1
print(res)
