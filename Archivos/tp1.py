import sys

from peculiar import misma_paridad, alterna_paridad, es_peculiar, n_esimo_peculiar, cant_peculiares_entre

def consola():
    nombre_funcion: str = sys.argv[1]
    numero_ingresado: int = int(sys.argv[2])

    if nombre_funcion == 'misma_paridad':
        if misma_paridad(numero_ingresado, numero_ingresado):
            print('si')
        else : 
            print('no')   
    elif nombre_funcion == 'alterna_paridad':
        if alterna_paridad(numero_ingresado):
            print('si')
        else:
            print('no')
    elif nombre_funcion == 'es_peculiar':
        if es_peculiar(numero_ingresado):
            print('si')
        else:
            print('no')
    elif nombre_funcion == 'n_esimo_peculiar':
        print(n_esimo_peculiar(numero_ingresado))

    elif nombre_funcion == 'cant_peculiares_entre':
        print(cant_peculiares_entre(numero_ingresado, numero_ingresado))                                        

consola()