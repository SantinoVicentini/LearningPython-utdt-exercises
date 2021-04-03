def misma_paridad(n:int, m:int) -> bool:
    '''
    Especificaciones: determinar si los parámetros son pares o impares
    Encabezado: def misma_paridad(n:int, m:int) -> str
    Precondiciones: n y m deben pertenecer a los N + {0}
    Postcondiciones: vr será un string “si” solo si ambos parámetros (n,m) son pares o impares, sin embargo, será “no” si difieren entre sí.
    '''
    vr:bool = True
    vr = vr and (n % 2 == 0 and m % 2 == 0 or n % 2 == 1 and m % 2 == 1)
    return vr


def alterna_paridad(n:int)->bool:
    '''
    Especificaciones: determinar si los digitos de un numero alternan su paridad
    Encabezado: def alterna_paridad(n:int) -> bool
    Precondiciones: n debe pertenecer a los N + {0}
    Postcondiciones: vr será 'True' si todos sus digitos alternan su paridad y será 'False' cuando dos digitos consecutivos tengan misma paridad.
    '''

    num:str = str(n)
    vr:bool = True
    
    i:int = 1
    while i < len(num):
        vr = vr and (int(num[i-1]) % 2 != int(num[i]) % 2)
        
        i = i + 1
         
    return vr


def es_peculiar(n:int)->bool:
    '''
    Especificaciones: determina un numero peculiar. Un numero peculiar es un 'n' multiplo de 22 y que a su vez sus digitos alternan paridad
    Encabezado: def es_peculiar(n:int) -> bool
    Precondiciones: n debe pertenecer a los N + {0}
    Postcondiciones: vr será 'True' si se trata de un 'numero peculiar' o 'False' si no lo es.
    '''
    vr:bool = True
    vr = vr and (n % 22 == 0 and alterna_paridad(n))
    return vr


def n_esimo_peculiar(n:int)->int:
    '''
    Especificaciones: Determina el n-esimo numero peculiar
    Encabezado: def n_esimo_peculiar(n:int) -> int
    Precondiciones: n debe pertenecer a los N + {0}
    Postcondiciones: vr será el numero peculiar de la posicion 'n'.
    '''
    vr:int = 0
    contador:int = 0
    i:int = 0
    while contador != n :
        i = i + 1 
        if es_peculiar(i):
            contador = contador + 1
            vr:int = i   
    return vr


def cant_peculiares_entre(n:int, m:int)->int:
    '''
    Especificaciones: Determina la cantidad de numeros peculiares que se encuentran en un rango de n a m inclusive.
    Encabezado: def cant_peculiares_entre(n:int, m:int) -> int
    Precondiciones: n y m deben pertenecer a los N + {0}
    Postcondiciones: vr será la cantidad de numeros peculiares que hay dentro de un rango de n inclusive hasta m inclusive.
    '''
    vr:int = 0
    i:int = n - 1
    contadorPec:int = 0
    while i < m:
        i+=1
        if es_peculiar(i):
            contadorPec += 1
            vr:int = contadorPec
    return vr
