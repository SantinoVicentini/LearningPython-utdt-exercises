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

print(misma_paridad(1,0))

def alterna_paridad(x:int)->bool:
    num:str = str(x)
    vr:bool = True
    
    i:int = 1
    while i < len(num):
        vr = vr and (int(num[i-1]) % 2 != int(num[i]) % 2)
        
        i = i + 1
         
    return vr
print(alterna_paridad(123455))