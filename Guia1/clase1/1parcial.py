from typing import List
def g(xs:List[str]) -> int:
    vr:int = 0
    while len(xs) > 0:
        x:str = xs.pop()
        if len(x) > 0:
            vr = vr + 1
    return vr

c:List[str] = ['a']
d:List[str] = c
n:int = 1
m:int = n
print(c, d, n, m)

c.append('b')
n = n*2
m = m + 5
print(c, d, n, m)

c.append('c')
m = g(d)
print(c, d, n, m)
