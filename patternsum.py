n = int(input())
res=n
num=2
for i in range(n-1,0,-1):
    res+=2*i*num
    num+=1
print(res)