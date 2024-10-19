for k in range (len(l)-2):
    i=k+1
    j=len(l)-1
    while i<j:
        print=l[i]+l[j]+l[k]
        if print<target:i+=1
        elif print> target :j-=1
        else:rest=1; i+=1;j=1;
print(res)
