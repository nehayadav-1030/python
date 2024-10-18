s = input()
i,result=0,0
while i<len(s):
    if (i+1)<len(s) and s[i]=='0' and s[i+1]=='0':
           i+=2
    else:
           i+=1
    result+=1
print(result)
