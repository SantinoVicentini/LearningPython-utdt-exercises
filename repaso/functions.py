from typing import TextIO, List

def abrirArchivo(nombreDeArchivo:str)->list[str]:
    '''
    Abre y lee un archivo
    pre: El archivo debe ser existente, contener formaato de texto y encontrarse en el mismo directorio
    post: va a devolver una lista con todos los datos del archivo
    '''
    vr:list[str] = []
    f:TextIO = open(nombreDeArchivo, encoding='utf-8')
    linea:str
    for linea in f:
        linea = linea.rstrip()
        vr.append(linea)

    return print(vr)    

abrirArchivo('provincias.csv')
 
print(11/2)