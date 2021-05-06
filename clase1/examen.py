from typing import List

def suma(lista:List[int]) -> int:
    n:int = 0
    i:int = 0
    while i < len(lista):
        n = n + lista[i]
        i = i + 1
    lista.clear()
    return n

lista: List[str] = ['w','l','g','r','x','t','t','m','z']
lista.pop()
lista.append('o')
if 'w' in lista:
    lista[0] = 'a'
elif 'g' in lista:
    lista[0] = 'b'
else:
    lista[0] = 'c'
print(lista)
lista.insert(3, lista[len(lista)-1])
lista[5] = 'i'
lista.pop(6)
print(lista)

a:List[int] = [1,2,3,4]
print(a, suma(a))
print(a, suma(a))
