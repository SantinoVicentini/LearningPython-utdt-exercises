from typing import List

#####################################################

def pos_minimo(L:List[int]) -> int:
    ''' Devuelve la posición del elemento mínimo de L. '''
    pos:int = 0
    j:int
    for j in range(0, len(L)):
        if L[j] < L[pos]:
            pos = j
    return pos

def selection_sort(A:List[int]):
    ''' Ordena (modifica) la lista A de menor a mayor. '''
    i:int
    for i in range(0, len(A)):
        sublista:List[int] = A[i:]
        pm:int = pos_minimo(sublista) + i
        A[i],A[pm] = A[pm],A[i]

#####################################################

A:List[int] = [59, 7, 388, 41, 2, 280, 50, 123]
print(A)
selection_sort(A)
print(A)

#####################################################

def pos_primer_mayor(x:int, L:List[int]) -> int:
    ''' Devuelve la posición del primer elemento >x en L. '''
    j:int
    for j in range(0, len(L)):
        if L[j] > x:
            return j
    return len(L)

def insertion_sort(A:List[int]):
    ''' Ordena (modifica) la lista A de menor a mayor. '''
    i:int
    for i in range(0, len(A)):
        x:int = A.pop(i)
        j:int = pos_primer_mayor(x, A[0:i])
        A.insert(j, x)

#####################################################

A:List[int] = [59, 7, 388, 41, 2, 280, 50, 123]
print(A)
insertion_sort(A)
print(A)

#####################################################
