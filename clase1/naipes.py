from typing import List
def buscar(corazon:str, a:List[str]) -> bool:
    vr:bool = False
    i:int = 0
    while i < len(a):
        if a[i] == corazon:
            vr = True
            break
        i += 1
    return vr
print(buscar('as', ['hola', 'sa']))