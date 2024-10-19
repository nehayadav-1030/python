A=input()
S=input()
total=0
for i in A:
    mn=100;d=0
    for j in S:
        d=abs(ord(i)-ord(j))
        if d<mn:
            mn=d
total+=mn
print(total)