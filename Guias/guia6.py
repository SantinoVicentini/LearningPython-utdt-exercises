from typing import List

#1
# mazo ordenado:
#   i = 1
#   vr = true
#   mientra i sea menor a len(mazo):
#       si m[i] es menor a m[i-1]:
#           vr = false
#       i+=1
#   devolver vr
def mazo(m:list[int])->bool:
    vr:bool = True          #O(1)
    i:int = 1               #O(1)
    while i < len(m):       #O(len(m)) O(M)
        if m[i] < m[i-1]:   #O(1)                       #O(M) lineal
            vr = False      #O(1)
        i+=1                #O(1)
    return vr               #O(1)
print(mazo([0,2,3,5]))


#2
# abrir los n cofres:
#   i = 0                                           O(1)
#   mientras que i sea menor a len(cofres):         O(N)
#       j = buscar la llave M para el cofre i       O(M)            O(N*M)
#       abrir el cofre i con la llave j             O(1)
#       i+=1                                        O(1)

#3
# cofre n con m ordenado:
#   i = 0
#   mientras que i sea menor a len(cofre):          O(N)
#       j = mazo ordenado M del cofre i             O(M)            O(N*M)
#       devolver i
#       i+=1

#4
#   llave m util para n cofres:
#   vr = 0
#   i = 0
#   mientras que i sea menor a len(cofres):
#       j = buscar la llave m para el cofre i       O(N*M)
#       abrir el cofre i con la llave j
#       devolver j
#       i+=1
