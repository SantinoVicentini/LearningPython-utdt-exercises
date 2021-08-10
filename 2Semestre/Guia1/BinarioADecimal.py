from typing import List, Tuple

def binAdec(b:str, n:int) -> int:
    vr:int = 0
    n = n-1
    i:int = 0
    while i < len(b):
        if b[i] == '1':
            vr = vr + (2**n)
        i += 1
        n -= 1
    
    return vr
print(binAdec('00010000', ))


