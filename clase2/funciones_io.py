from typing import TextIO, List

###################################################################

def leer_archivo(file:str) -> List[str]:
    '''
    Abre y lee un archivo de entrada llamado file (con codificación utf-8) ubicado en el mismo directorio,
    donde cada palabra esta separada por un '\n', y devuelve una lista de strings.
    Pre: file es el nombre de un archivo de texto con codificación utf-8, donde cada línea representa una palabra s.
    Post: vr toma como valor una lista de strings con todas las palabras por presentes en el archivo de entrada.
    '''

    f:TextIO = open(file, encoding='utf-8')
    text:str = f.read()
    vr:List[str] = text.split('\n')
    

    return vr

leer_archivo('ejemplo_batalla_freestyle.txt')


###################################################################



def longitud_promedio(file:str) -> float:
    '''
    Computa la longitud promedio de las palabras presentes en el archivo de entrada.
    Pre: file es el nombre de un archivo de texto, donde cada línea representa una palabra s.
         len(s)>0; s tiene solamente letras en minúscula: abcde...xyz, sin tildes, diéresis ni eñes.
    Post: vr toma como valor la longitud promedio de las palabras presentes en el archivo de entrada.
    '''
    texto:List[str] = leer_archivo(file)
    total:int = 0
    i:int = 0
    linea:str
    for linea in texto:
        total = total + len(linea)
        i += 1
    vr:float = total/i
    return vr

print(longitud_promedio('ejemplo_batalla_freestyle.txt'))




###################################################################

from funciones import letras_ordenadas


def devuelve_palabras_ordenadas(file:str) -> List[str]:
    '''
    Dado un archivo de texto, muestra por pantalla las palabras que se encuentran ordenadas alfabéticamente.
    Pre: file es el nombre de un archivo de texto, donde cada línea representa una palabra s.
         len(s)>0; s tiene solamente letras en minúscula: abcde...xyz, sin tildes, diéresis ni eñes.
    Post: imprime por pantalla aquellas palabras s del archivo de entrada que mantienen orden alfabético.
    '''
    vr:list[str] = []
    texto:List[str] = leer_archivo(file)
    linea:str
    for linea in texto:
        if letras_ordenadas(linea):
            vr.append(linea)
    return vr

    
        


devuelve_palabras_ordenadas('ejemplo_batalla_freestyle.txt')




###################################################################

def guardar_palabras_ordenadas(file:str) -> None:
    '''
    Dado un archivo de texto, guarda en palabras_ordenadas.txt aquellas palabras que se encuentran ordenadas alfabéticamente.
    Pre: file es el nombre de un archivo de texto, donde cada línea representa una palabra s.
         len(s)>0; s tiene solamente letras en minúscula: abcde...xyz, sin tildes, diéresis ni eñes.
    Post: genera un archivo .txt de salida donde cada línea corresponde a una palabra s que se encuentra ordenada alfabéticamente.  
    '''
    f:TextIO= open('palabras_ordenadas.txt', 'w', encoding='utf-8')
    palabras_ordenadas:list[str] = devuelve_palabras_ordenadas(file)
    linea:str
    for linea in palabras_ordenadas:
        f.write(linea + '\n')
    f.close()

guardar_palabras_ordenadas('ejemplo_batalla_freestyle.txt')




