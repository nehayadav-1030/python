inp1=int(input())
inp2=int(input())
arr=list(map(int,input().split()))
mx=0
for i in range(0,len(arr)-1):
    temp=arr[i:inp2+1]
    k,s=1,0
    for j in temp:
        s=s+(k*j)
        k=k+1
    if s>mx:
       mx=s
print()


