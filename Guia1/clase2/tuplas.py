from typing import List, Dict, Tuple, Set

clorinda = [( " Dorotea " , 14581 , 82) , ( " Azucena " , 27652 , 75) ,
( " Dorotea " , 3245 , 89) , ( " Felisberto " , 987 , 90) ]
pirane = [( " Azucena " , 8613 , 87) , ( " Dorotea " , 5821 , 88) ,
( " Felisberto " , 2854 , 89) , ( " Luis " , 99899 , 35) ]
mosconi = [( " Dorotea " , 42939 , 67) , ( " Luis " , 1150 , 90) ]

personas = [( " Maria " , 123456 , 25) ,
( " Ahmed " , 6841635 , 81) ,
( " Jairo " , 123456 , 65) ,
( " Matias " , 355128 , 90) ,
( " Tomas " , 355120 , 8) ,
( " Matias " , 355128 , 48) ]




def formosa(localidad1:List[tuple[str, int, int]], localidad2:List[tuple[str, int, int]]) -> List[str]:
    nombresaprobados:set[str] = set()
    nombresaprobados2:set[str] = set()
    i:int = 0
    j:int = 0
    while i < len(localidad1):
        if localidad1[i][2] > 80:
            nombresaprobados.add(localidad1[i][0])
        i+=1
    while j < len(localidad2):
        if localidad2[j][2] > 80:
            nombresaprobados2.add(localidad2[j][0])
        j+=1
    union:set[str] = nombresaprobados & nombresaprobados2
    ordenadoAlfabeticamente:set[str] = sorted(union)
    vr:List[str] = list(ordenadoAlfabeticamente)
    return vr

print(formosa(clorinda, pirane))

personas = [( " Maria " , 123456 , 25) ,
( " Ahmed " , 6841635 , 81) ,
( " Jairo " , 123456 , 65) ,
( " Matias " , 355128 , 90) ,
( " Tomas " , 355120 , 8) ,
( " Matias " , 355128 , 48) ]
    

def dni_mellizos(personas:list[tuple[str, int, int]]) -> Dict[int, List[tuple[str, int]]]:
    dict_personas:Dict[int, List[tuple[str, int]]] = dict()
    persona:int
    for persona in personas:
        if persona[1] in dict_personas.keys():
            dict_personas[persona[1]].append((persona[0], persona[2]))
        else:
            dict_personas[persona[1]] = [(persona[0], persona[2])]
    
    dnis_mellizos:Dict[int, List[tuple[str, int]]] = dict()
    clave:int
    valor:List[tuple[str, int]]
    for clave, valor in dict_personas.items():
        if len(valor) > 1:
            dnis_mellizos[clave] = valor
    return dnis_mellizos

print(dni_mellizos(personas))

        
