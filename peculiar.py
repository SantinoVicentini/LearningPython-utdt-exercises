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
    return vr

#print(misma_paridad(4,4))

def alterna_paridad(x:int)->str:
    num:str = str(x)
    vr:str = ''
    numAnterior:int = int(num[0]) % 2
    if x < 10:
        vr = 'si'

    i:int = 1
    while i < len(num):
        if numAnterior != int(num[i]) % 2:
            numAnterior = int(num[i]) % 2
            i = i + 1
            vr = 'si'
        else:
            vr = 'no'
            break
    return vr
print(alterna_paridad(101011))