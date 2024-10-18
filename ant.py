n=int(input())
l=(map(int,input().split()))
#print(l)
pos=0
result=0
for i in l:
    pos+=i
    if pos==0:
        result+=1
print(result)