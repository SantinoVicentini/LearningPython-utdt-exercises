from typing import List
def f ( x :int , y : int ) -> int :
    x = 2 * x + y
    return x

x : int = 3
y : int = 7
y = f (y , x )
x = f (y , x )
#print (x , y )
#print (x , x * x )

def f2c(x:int)-> float:
    '''
    Convierte de grados Farenheit en grados Celcius.
    pre: x=int.
    post: vr es el resultado, redondeado a dos decimales de la operacion
    para convertir grados farenheit en celcius.
    '''
    x:float = (x-32) * 5/9
    return round(x)
print(f2c(1))  

def tabla(x:int):
    '''
    imprime una tabla de conversion de grados f en c en un intervalo de 0 a 120 de a 10 
    pre: 0 =< x >= 120
    post: vr es el resultado de imprimir por pantalla los grados de 0 a 120 de 10 en 10                     #predicado I : x
    '''                                                                                                         
    x:int = 0                                                                                               # x vale 0
    while x <= 120: #inicio del ciclo empezando en 0 hasta el 120 inclusive
        print(x)    #x vale 0 por lo tanto es menor que 120, entra al ciclo imprime el valor de x, luego imprime la conversion de f a c de x 
        print(f2c(x))
        x = x + 10    # x pasa a valer 10 xq 0 + 10 = 10 // se repite el ciclo pero ahora con el 10, pasa la verificacion y entra en el ciclo. asi hasta que la x valga 130 y no cumpla la condicion, por lo tanto sale del bucle y no se sigue ejecutando
#tabla(x)       
   
def es_palindromo(word:str)->bool:
    '''
    determina si la palabra en cuestion se trata de un palindromo
    pre: word sea un string y != null
    post: vr va a ser verdadero o falso dependiendo de si la palabra es un palindromo
    '''
    vr:bool = True
    lenght = len(word)
    beg:str = word[0]
    end:str = word[lenght - 1]
    i:int = 0  
    while i < lenght:
        if beg == end:
            i += 1
            beg = word[i]
            lenght = lenght - 1
            end = word[lenght - 1]
            vr
        else:
            vr = False
            break
    return vr

 
print(es_palindromo('oso'))                

def es_primo(x:int)->bool:
    vr:bool = True
    i:int = 0
    contador:int = 0
    while i < x:
        i +=1
        if x % i == 0:
            contador = contador + 1
        if contador > 2:
            vr = False
        else:
            vr
    return vr


print(es_primo(8))


def hola(s)->str:
    j : int = 1
    rv = 'si'
    while j < len(s):
        if s[j-1] < s[j]:
            j += 1
            rv
        else:
            rv = 'no'
            break
    return rv        
            

print(hola('acfjkpva'))
'''
s : str = 'acfjkpvzqta'
j : int = 0
while s [ j ] < s [ j +1] and j <len( s ) -1:
    j = j + 1
if j == len( s ) :
    print ( ' Las letras están ordenadas alfabéticamente ')
else :
    print ( ' Las letras no están ordenadas alfabéticamente ')

'''






#Ejemplos
#75 == 23.98
#73 == 22.78
#72 == 22.22
#71 == 21.67
#70 == 21.11

#EJERCICIO 3 GUIA 2
#a 

def a(n:float)->int:
    '''
    Covierte a un numero en su parte entera
    pre: n > 0 || n = 0
    post: vr es igual al resultado de round(n) que devuelve su parte entera
    '''
    vr:int = 0
    vr = vr + round(n)
    return vr
print(a(2.20))

#b

def b(n:int)->int:
    '''
    calcula el factorial de n
    pre: n > 0 || n = 0
    post: vr es igual al resultado de la multiplicacion de los numeros
    anteriores a n, incluyendo n
    '''
    vr:int = 1
    i:int = 1
    while i <= n:
        vr = vr * i
        i+=1
    return vr
print(b(5))

#c

def c(n:int, k:int)->int:
    '''
    calcula el combinatorio de n y k
    pre: n, k > 0 && k < n || k = n
    post: vr es igual al resultado de la division entre el factorial de n
    y el factorial de k multiplicado n - k
    '''
    vr:int = b(n)//b(k)*(n-k)
    if n == 0 and k == 0:
        vr = 1
    return vr
print(c(0,0))
#d

def d(n:int)->str:
    '''
    devuelve un string con los valores de n para todo 0 <= i <= n
    pre: n >= 0
    post: vr va a devolver una cadena de strings separadas con comas con los numeros que cumplen esas condiciones
    '''
    vr:str = ''
    i:int = 0
    while i <= n:
        vr = vr + str(i) + ', '
        i+=1
    return vr
print(d(3))
#e

def e(n: int)->str:
    '''
    devuele un string con n asteriscos
    pre: n>=0
    post: vr devuelve un string con n asteriscos
    '''
    vr:str = ''
    i:int = 0
    while i < n:
        vr = vr + '*'
        i+=1
    return vr
print(e(4))
#f

def f(n:int)-> str:
    '''
    toma un n y lo transforma en asteriscos
    pre: n >=0
    post: vr es igual a n = *
    '''
    n:str = '*'
    vr = n
    return vr
print(f(2))
#g

def g(s:str)->str:
    '''
    toma un texto y devuelve la inversa del mismo
    pre: s !null
    post: vr es igual a la inversa de un s dado
    '''
    vr:str = ''
    i:int = 1
    while i < len(s):
        vr = vr + s[len(s)-i]
        i+=1
    vr = vr + s[0]
    return vr
print(g('soyretarado'))
#h

def h(s:str)->int:
    '''
    toma un texto y cada vez que encuentra una 'a' , le suma uno al contador
    pre: s !null
    post: vr es igual al resultado de la suma de 'a' en s
    '''
    vr:int = 0
    i:int = 0
    j=int = 0
    contador:int = 0
    while i < len(s):
        if 'a' == s[i]:
            contador+=1
        i+=1
    vr = contador
    return vr
print(h('holaaaa'))
#i 
'''
def i(s:str, t:str)->int:
    cuenta la cantidad de veces que s esta contenido en t y lo suma a un contador
    pre: none
    post: vr es igual a la suma de todas las veces que s esta contenida en t
#j
'''
'''
def j(n:int)->str:
    recibe un numero y devuelve su representacion binaria
    pre: n>=0
    post: vr es igual a la suma del resto de cada division de n por 2 
'''   
#k
'''
def k(s:str)->int:
    recibe un string con numeros en base 2 y lo convierte a un numero entero
    pre: s !null && los numeros de s >=0
    post: vr es igual a la suma de las potencias con base 2 y exponente = a la longitud del string + 1
'''
    

#------------------------------------------------------------------------------------------------------------------------
#Guia 3
#ej 1 a)
'''
(I) True ---> bool
(II) not False ---> true bool
(III) 1 > 0 ---> true bool
(IV) not ('aa' < 'ab') ---> false bool
(V) 1 > 0 or not 'aa' < 'ab' true
(VI) 5.6 > 2.0 and len('hola') < 2 false
(VII) 5.6 > 2.0 or len('hola') < 2 true
(VIII) int('3') - 1 == len('x' * 2) true

'''
#2
'''
p =True
q =False

if p :
    if q :
        print ( 'A ')         #p(t)q(t) A p(t)q(f) B p(f)q(t)   p(f)q(f)   
    else :
        print ( 'B ')



if p :
    if q :
        print ( 'A ')         #p(t)q(t) A p(t)q(f)  p(f)q(t) B p(f)q(f) B
else :
    print ( 'B ')


## Dif indentacion del else

if p and q:
    print ( 'A ')
elif p or q:
    print ( 'B ')

if p and q:
    print ( 'A ')
elif not p or q:
    print ( 'B ')
'''
def suma_en_pos_impares(l:List[int], n:int) -> List[int]:
    vr:List[int] = []
    i:int = 0
    while i < len(l):

        if i % 2 == 1:

            vr.append(l[i]+n)
        else:


            vr.append(l[i]) 
        i += 1   
    return vr
print(suma_en_pos_impares([1,2,3,4], 2))

