def inverso(x: float) -> float:
  ''' Devuelve la división de 1 por x.
  Precondición: x!=0
  Postcondición: vr es igual al resultado de dividir 1 por x.
  '''
  return 1/x * x

#error semantico 1/x

def cuadrado(n: int) -> int:
  ''' Devuelve n elevado al cuadrado.
  Precondición: Ninguna.
  Postcondición: vr es igual a n elevado al cuadrado.
  '''
  return n*n

#error semantico n**n

n:int = 3
print("El cuadrado de", n, "es", cuadrado(n))#error de sintaxis cuardado

#n:int = "hola" #error tiempo de ejecucion no puede elevar un string
print("El cuadrado de", n, "es", cuadrado(n))

x:float = 2.0
print("El inverso de", x, "es", inverso(x))#error de sintaxis )

x:float = 1.0#error tiempo de ejecucuion, no se puede dividir por 0 #error de sintaxis o
print("El inverso de", x, "es", inverso(x))#error de tiempo de ejecucion X

