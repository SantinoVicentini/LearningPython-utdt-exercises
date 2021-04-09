from typing import List

def nave_cercana(sensado:list[int], p:int)->bool:
    vr:bool = False
    i:int = 0
    while i < len(sensado):
        if sensado[i] <= p:
            vr = True
        i += 1
    return vr
print(nave_cercana([51, 52, 55], 50))

