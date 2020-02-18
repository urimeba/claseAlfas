"""
ESTRUCTURA DE UNA FUNCION EN PYTHON
def nombre_de_la_funcion(argumentos):
    operacion
    operacion2
    return algun_numero

nombre = input("Ingresa tu nombre: ")

def saludo(n):
    print( "Hola " + n + "!!")
    return None
salpudo(nombre)
"""
"""
numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))
#def suma(numero1, numero2):
 #   return numero1 + numero2

def resta(numero1=10, numero2=5):
    return numero1 - numero2

print(resta(numero1))
"""
"""
def posicional(*argumentos):
    for arg in argumentos:
        print(arg)

    return None

posicional(1, "Argumento posicional #2")
"""

""""
def nombre(**z):
    for argumento in z:
        print(str(argumento) + " = "  + str(z[argumento]))

    return None
nombre(a=1, b="Hola", c="Adios", d=4.2)
"""


"""
Pasar varios argumentos con o sin nombre
Para los argumentos sin nombre, debera imprimir su valor
Para los argumentos con nombre, debera imprimir el nombre y su valor
"""
def combinacional(*args, **kwargs):
    suma = 0
    for arg in args:
        suma += arg

    print("Suma= " + str(suma))

    for kwarg in kwargs:
        print(str(kwarg) + "=" + str(kwargs[kwarg]))


combinacional(2, 4, 6, a="A", b="B", c="C")

