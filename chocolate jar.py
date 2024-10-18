l=list(map(int,input().split()))
n=int(input())
a=0
for i in l:
    if i%3==0:
        a+=i//3
    
    if i%3>0:
         a+=i//3+1
print(a)