from math import gcd
s1 = input()
s2 = input()
tmp1 = s1
tmp2 = s2
len1 = len(s1)
len2 = len(s2)
lcm = 0
def lcms(x, y):
    return (x * y) // gcd(x, y)
lcm = lcms(len1, len2)
while len(s1) < lcm:
    s1 += tmp1
while len(s2) < lcm:
    s2 += tmp2
if s1 == s2:
    print(1)

else:
    print(0)

