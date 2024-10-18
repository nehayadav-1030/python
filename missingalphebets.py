s=input().lower()
alpha='abcdefghijklmnopqrstuvwxyz'
res=' '
for i in alpha:
    if i not in s:
        res+=i
print(res)