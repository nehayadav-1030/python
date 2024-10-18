n=input()
s=input().split()
z=float('inf')
idx=s.index(n)

for i in range (len(s)):
    if s[i]=='-':
        z=min(z,abs(i-idx)-1)
    if  i==0 or i==len(s):
        z=min(z,abs(i-idx))
print(z)