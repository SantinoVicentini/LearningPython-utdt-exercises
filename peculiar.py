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
    
    i:int = 1
    while i < len(num):
        vr = vr and (num[i-1] != num[i])
        
        i = i + 1
         
    return vr
print(alterna_paridad(10122))