import sys

from typing import List

def listaOrdenada(a:List[int]) -> bool:
    vr:bool = True
    i:int = 1
    while i < len(a):
        if a[i] < a[i-1]:
            vr = False  
            break
        i += 1
    return vr

def g(s:str)->str:
    '''
    toma un texto y devuelve la inversa del mismo
    pre: s !null
    post: vr es igual a la inversa de un s dado
    '''
    vr:str = ''
    i:int = 1
    while i < len(s):
        vr = vr + s[len(s)-i]
        i+=1
    vr = vr + s[0]
    return vr

def permitidos(s:str)->bool:
    i:int = 0
    numeros:List[str] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    vr:bool = True
    while i < len(s):
        vr = vr and s[i] in numeros
        i+=1
    return vr

def numeros()->List[str]:
    vr:List[str] = []
    i:int = 1
    while i <= 999999:
        vr.append(str(i))
        i += 1
    return vr

def permitidosv(a:List[str])->bool:
    i:int = 0
    numeross:List[str] = numeros()
    vr:bool = True
    while i < len(a):
        if a[i] in numeross:
            vr
        else:
            vr = False
        i +=1
    return vr

def consola():
    nombre_funcion:str = sys.argv[1]
    
    if nombre_funcion == 'listaOrdenada':
        i:int = 2
        lista = []
        while i < len(sys.argv):
            lista.append(sys.argv[i])
            i+=1
        sys.argv.insert(2, lista)
        if permitidosv(lista) and listaOrdenada(lista):
            print('ordenanda')
        elif not permitidosv(lista):
            print('error en el caracter ingresado')



    elif nombre_funcion == 'g':
        if len(sys.argv) > 3 or not permitidos(sys.argv[2]):
            print('no')
        else:
            arg:str = sys.argv[2]
            print(g(arg))
        



consola()

