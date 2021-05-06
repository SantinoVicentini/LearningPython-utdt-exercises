from typing import List
#3)a)
def maximoElemento(a:List[float]) -> float:
    i:int = 1
    vr:float = 0.0
    while i < len(a):
        if a[i] > a[i-1]:
            contador = a[i]
        i+=1
    vr = contador
    return vr
print(maximoElemento([1.3, 2, 2.1]))             

#b)
def concatenacion(a:List[str]) -> str:
    vr:str = ''
    i:int = 0        
    while i < len(a):
        vr = vr + a[i]
        i+=1
    return vr
print(concatenacion(['abc', '', 'def', 'g']))

#c)
def listaOrdenada(a:List[int]) -> bool:
    vr:bool = True
    i:int
    for i in range(0, len(a)):
        vr = vr and a[i] < a[i-1]
        break
    return vr
print(listaOrdenada([1,2,0]))

#d)
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
print(numerosImpares(2))    

#e)
def suma_de_elementos(a:List[int], n:int) -> List[int]:
    vr:List[int] = []
    i:int = 0
    while i < len(a):
        vr.append(a[i] + n)
        i+=1
    return vr
print(suma_de_elementos([1], 1))

#f)
def contarCaracteres(a:List[str]) -> int:
    vr:str = ''
    i:int = 0
    while i < len(a):
        vr = vr + a[i]
        i+=1
    return len(vr)
print(contarCaracteres(['ho','la','beba'])) 

#g)
def letras(a:list[str], letra:str) -> int:
    vr:int = 0
    i:int = 0
    j:int = 0
    contador:str = ''
    while i < len(a):
        contador = contador + a[i]
        i+=1
        while j < len(contador):
            if letra == contador[j]:
                vr+=1
            j+=1
    return vr
print(letras(['hotoooa', 'ttdo', 'bien?'], 'o'))

#h)
def separar(txt:str, sep:str) -> List[str]:
    vr:List[str] = []
    i:int = 0
    while i < len(txt):
        if sep == txt[i]:
            vr=txt.split(sep)
        i+=1
    return vr
print(separar('hola;todo;bien?', ';'))

def suma_problematica ( lista : List [ int ]) -> int:
    n :int = 0
    i :int = 0
    while i < len( lista ) :
        n = n + lista [ i ]
        i = i + 1
    lista = [] # clear () elimina todos los elementos de la lista .
    return n

#9)
def cuentaRegresiva ( n : int ) -> List[int] :
    vr : List [str] = []
    i:int
    for i in range(n):
        vr.append(str(n-i))
    vr.append(' despegue ')
    return vr
print(cuentaRegresiva(3))

def suma_de_enteros ( a : List[float] ) -> int :
    vr : int = 0
    i :int = 0
    for i in range(len(a)):
        vr = vr + round(a[i])
    return vr
print(suma_de_enteros([1.2,2.5,1.0,12.2]))

def listaRegresiva ( a : List[int] ) -> List[int] :
    vr : List [int] = []
    i :int
    for i in range(len(a)):
        vr.append(len(a)-i)
    return vr
print(listaRegresiva([1,2,3,4,5,6]))

def buscar_v1 ( elem :int , lista : List [int ]) -> bool :
    ''' Determina si elem está en la lista .
    Pre : Ninguna .
    Post : vr equivale a que elem aparece al menos una vez en la lista .
    '''
    vr : bool = False
    i :int
    for i in range(len(lista)):
        vr = vr or elem == lista[i]
    return vr

def buscar_v2 ( elem :int , lista : List [int ]) -> bool :
    ''' Determina si elem está en la lista .
    Pre : Ninguna .
    Post : vr equivale a que elem aparece al menos una vez en la lista .
    '''
    vr : bool = False
    i :int
    for i in range(len(lista)) :
        if elem == lista[i] and not vr:
            vr = lista[i] == elem
            
    return vr

a : List [int] = [1 ,2 ,4 ,1 ,5]
print ( buscar_v1 (1 , a ) , buscar_v2 (1 , a ) )
print ( buscar_v1 (3 , a ) , buscar_v2 (2 , a ) )
print ( buscar_v1 (5 , a ) , buscar_v2 (5 , a ) )

def primeraOcurrencia(elem:int, a:List[int]) -> int:
    i:int
    vr:int = 0
    for i in range(len(a)):
        if elem != a[i]:
            vr += 1
            break
    return vr
print(primeraOcurrencia(2, [1,2,3,2,3]))