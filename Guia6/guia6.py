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

#6
def bubblesort(a:List[int]):
    i:int
    j:int 
    for j in range(len(a)-1):
        for i in range(len(a)-1-j):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a



def busqueda(a:List[int], x:int):
    ordenada:list[int] = bubblesort(a)
    i:int = 0
    while i < len(a):
        if x == a[i]:
            return a[:i+1]
        i+=1
print(busqueda([20,3,10,6,5,2,1], 10))


#7b
def busquedaa(a:List[int], x:int):
    i:int = 0
    while i < len(a):
        if x == a[i]:
            return a[:i+1]
        i+=1
print(busquedaa([1,2,3,4,5,6,7,9,10,11], 11))

def busquedaOrdenada(a:list[int], x:int):
    left:int = 0
    right:int = len(a)
    while left < right:
        mid:int = (left + right) // 2
        if x == a[mid]:
            return a[:mid+1]
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid
    return(a[:left])

print(busquedaOrdenada([1,2,3,4,5,6,7,9,10,11], 11))
        
#8
#a
def promedio(a:List[int]) -> float:
    i:int = 0
    vr:Float = 0
    while i < len(a):
        vr = vr + a[i] / len(a)
        i+=1
    return vr
print(promedio([1,2,3,4,5,6])) 

#b
def mediana(a:List[int]) -> int:
    vr:int = 0
    i:int = 0
    while i < len(a):
        ordenada:List[int] = bubblesort(a)