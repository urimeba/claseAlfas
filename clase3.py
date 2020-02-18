"""
Ejercicio #1 - TRY-CATCH
try:
    haz_algo_si_no_hay_error
except Exception as tu_variable_de_error :
    haz_algo_con_el_error

Revisa el codigo y verifica por que marca error.
Instancia una sentencia TRY-CATCH para evitar que el programa rompa y manda un mensaje de error 
personalizado, explicando el problema con la operacion. 
"""
"""
numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))

try:
    print(numero1/numero2)
except ArithmeticError as err:
    print("Esta operacion no pudo ser realizada")
    print("Error: " + str(err))

"""


"""
EJERCICIO #2 - LAMBDA

Estructura de una funciona lambda:
lambda argumento1, argumento2, n_argumentos : haz_alguna_operacion

Escribe una funcion que sume 10 y lo multiplique por 2 a un numero pedido al usuario
"""

#numero = int(input("Ingresa un numero: "))
#numero2 = int(input("Ingresa otro numero: "))
#numero3 = int(input("Ingresa otro numero: "))

# resultado = lambda numero, numero2, numero3: numero + numero2 + numero3
# print(resultado(numero, numero2, numero3))

"""
EJERCICIO #4 - LAMBDA
Escribe una funcion que  pida al usuario numero1, numero2 y numero3.
Al numero 3 lo elevara al cuadrado y luego, sera sumado al numero1 y 
numero2
"""

#resultado = lambda x, y, z:  (z*z) + x + y
#print(resultado(numero, numero2, numero3))

"""
EJERCICIO #5 - MAP
Estructura de la funcion MAP:
map(funcion_a_realizar, estructura_de_dato)

Luego, mediante map, pasale la siguiente lista como parametro, imprimiendo los resultados
"""
"""
numeros = [2,3,4,5]

def cuadrado(numero):
    return numero * numero

print(list(map(cuadrado, numeros)))
"""

"""
EJERCICIO #6 - MAP y LAMBDA
Resuelve el problema anterior usando MAP y LAMBDA
"""
# map(funcion_a_realizar, estructura_de_datos)
# resultado = lambda argumento1, argumentoN:  argumento1 + argumento2
numeros = [2,3,4,5]
resultado = list(map(lambda n: n*n, numeros))
print(resultado)
