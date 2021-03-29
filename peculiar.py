def misma_paridad(n:int, m:int) -> bool:
    '''
    Especificaciones: determinar si los parámetros son pares o impares
    Encabezado: def misma_paridad(n:int, m:int) -> str
    Precondiciones: n y m deben pertenecer a los N + {0}
    Postcondiciones: vr será un string “si” solo si ambos parámetros (n,m) son pares o impares, sin embargo, será “no” si difieren entre sí.
    '''
    if n % 2 == 0 and m % 2 == 0 or n % 2 == 1 and m % 2 == 1: 
        vr = True
    else: 
        vr = False
    return vr

#print(misma_paridad(4,4))

def alterna_paridad(x:int)->bool:
    num:str = str(x)
    vr:bool = True
    numAnterior:int = int(num[0]) % 2
    
    i:int = 1
    while i < len(num):
        if numAnterior != int(num[i]) % 2:
            numAnterior = int(num[i]) % 2
            i = i + 1
            vr
        else:
            vr = False
            break
    return vr
print(alterna_paridad(123455))