n=int(input())
l=list(map(int,input().split()))
p=int(input())
primes=[]
res=0
for i in range(2,int(n**0.5)+1,2):
    while n%i==0:
        primes.append(i)
        n/=2
print(primes)
for l in set(primes):
    if l<len(l):
        res+=primes.count(i)*l(i)
print(res)