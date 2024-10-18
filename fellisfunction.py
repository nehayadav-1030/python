n=int(input())
l=[1,1]
for i in range(2,n+1):
    l.append(int(l[i-1]+l[i-2]*7+i/4)%(10**9+7))
print(l[n])