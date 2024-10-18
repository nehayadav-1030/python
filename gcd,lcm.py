"""def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
print(gcd(12,18))"""

a=int(input())
b=int(input())
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
print(gcd(a,b))
print(a*b//gcd(a,b))
