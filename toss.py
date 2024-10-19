S=input()
SC,HC=0,0
for i in S:
    if i=='H':
        SC+=2
        HC+=1
        if HC==3:
            break
    else:SC-=1
print(SC)