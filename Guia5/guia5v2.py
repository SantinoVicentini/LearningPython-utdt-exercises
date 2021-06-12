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

    
def new(file:str, nuevo:str):
    archivo:List[str] = leer(file)
    i:int
    w:TextIO = open(nuevo, 'w', encoding='utf-8')
    for i in archivo:
        w.write(str(len(i)) + '\n')
new('provincias.csv', 'pruebaaa.txt')

def primo(n:int)->bool:
    vr:bool = True
    i:int = 0
    contador:int = 0
    if n == 1:
        vr = False
    while i < n:
        i +=1
        if n % i == 0:
            contador = contador + 1
        if contador > 2:
            vr = False
        else:
            vr
    return vr

def primos(n:int, nuevo:str):
    i:int = 1
    w:TextIO = open(nuevo, 'w', encoding='utf-8')
    while i <= n:
        if primo(i):
            w.write(str(i) + '\n')
        i+=1
primos(97, 'primosss.txt')

def prefijo(s:str)->str:
    vr:str = ''
    i:int = 0
    while i < len(s):
        vr = vr + s[i]
        if s[i] == '#':
            vr = vr.rstrip('#')
            break
        i+=1
    return vr
print(prefijo('#asas'))

def crear(file:str, nuevo:str):
    archivo:List[str] = leer(file)
    i:str
    w:TextIO = open(nuevo, 'w', encoding='utf-8')
    for i in archivo:
        w.write(prefijo(str(i)) + '\n')
crear('archivo.py', 'creando.py')

