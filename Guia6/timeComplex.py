from typing import List

def numerosImpares(n:int) -> List[int]:
    i:int=0
    vr:List[int] = []
    contador:List[int] = []
    while i < n*n:
        if i % 2 == 1:
            contador.append(i)
        i+=1
    vr = contador[0:n]
    return vr

import time 
n:int = 0
ns:List[int] = []
ts:List[float] = []
res:List[int] = []
while n <= 1000:
    comienzo:float = time.time()
    res = numerosImpares(n)
    ns.append(n)
    ts.append(time.time() - comienzo)
    n = n + 10

##############
import  as plt
plt.plot(ns, ts)
plt.xlabel('n')
plt.ylabel('tiempo')
plt.show()