from typing import List, TextIO

def leer(file:str) -> List[str]:
    f:TextIO = open(file, encoding='utf-8')
    text:str = f.read()
    vr:List[str] = text.split('\n')
    return vr

def longitud(file:str) -> List[int]:
    archivo:List[str] = leer(file)
    i:int
    vr:List[int] = []
    for i in archivo:
        vr.append(len(i))
    return vr
print(longitud('provincias.csv'))
    

