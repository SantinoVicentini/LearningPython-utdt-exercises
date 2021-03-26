
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
    return round(x, 2)


#Ejemplos
#75 == 23.98
#73 == 22.78
#72 == 22.22
#71 == 21.67
#70 == 21.11

#EJERCICIO 3 GUIA 2
#a 
'''
def a(n:float)->int:
    Covierte a un numero en su parte entera
    pre: n > 0 || n = 0
    post: vr es igual al resultado de abs(n) que devuelve su parte entera
'''
#b
'''
def b(n:int)->int:
    calcula el factorial de n
    pre: n > 0 || n = 0
    post: vr es igual al resultado de la multiplicacion de los numeros
    anteriores a n, incluyendo n
'''
#c
'''
def c(n:int, k:int)->int:
    calcula el combinatorio de n y k
    pre: n, k > 0 && k < n || k = n
    post: vr es igual al resultado de la division entre el factorial de n
    y el factorial de k multiplicado n - k
'''
#d
'''
def d(n:int)->str:
    devuelve un string con los valores de n para todo 0 <= i <= n
    pre: n >= 0
    post: vr va a devolver una cadena de strings separadas con comas con los numeros que cumplen esas condiciones
'''
#e
'''
def e(n: int)->str:
    devuele un string con n asteriscos
    pre: n>=0
    post: vr devuelve un string con n asteriscos
'''
#f
'''
def f(n:int)-> str:
    toma un n y lo transforma en asteriscos
    pre: n >=0
    post: vr es igual a n = *
'''
#g
'''
def g(s:str)->str:
    toma un texto y devuelve la inversa del mismo
    pre: s !null
    post: vr es igual a la inversa de un s dado
'''
#h
'''
def h(s:str)->int:
    toma un texto y cada vez que encuentra una 'a' , le suma uno al contador
    pre: s !null
    post: vr es igual al resultado de la suma de 'a' en s
'''
#i 
'''
def i(s:str, t:str)->int:
    cuenta la cantidad de veces que s esta contenido en t y lo suma a un contador
    pre: none
    post: vr es igual a la suma de todas las veces que s esta contenida en t
'''
#j
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
    

    
    

