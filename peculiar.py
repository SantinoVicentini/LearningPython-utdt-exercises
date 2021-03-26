def misma_paridad(n:int, m:int) -> str:
    '''
    Especificaciones: determinar si los parámetros son pares o impares

    Encabezado: def misma_paridad(n:int, m:int) -> str

    Precondiciones: n y m deben pertenecer a los N + {0}

    Postcondiciones: vr será un string “si” solo si ambos parámetros (n,m) son pares o impares, sin embargo, será “no” si difieren entre sí.
    '''

    if n % 2 == 0 and m % 2 == 0 or n % 2 == 1 and m % 2 == 1: 
        vr = 'si'

    else: 
        vr = 'no'
    
    return print(vr)    

misma_paridad(5,4)
    
#def alterna_paridad(x:int) -> str:

