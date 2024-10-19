x,y=int(input()),int(input())
while y>0:
    if x<y:
        x,y=y,x
    else:
        t=x-y
        x=y
        y=t
print(x)