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
# print(10/0)


"""
EJERCICIO #2 - LAMBDA

Estructura de una funciona lambda:
lambda argumento1, argumento2, n_argumentos : haz_alguna_operacion

Escribe una funcion que sume 10 y lo multiplique por 2 a un numero pedido al usuario
"""
# numero = int(input("Ingresa un numero: "))
# resultado = lambda numero : (numero + 10) * 2
# print(resultado(numero))

"""
EJERCICIO #3 - LAMBDA
Escribe una funcion que multiplique un numero1 y un numero2 pedidos al usuario
"""
# numero1 = int(input("Ingresa un numero: "))
# numero2 = int(input("Ingresa otro numero: "))
# resultado = lambda numero1, numero2 : numero1 * numero2
# print(resultado(numero1, numero2))

"""
EJERCICIO #4 - LAMBDA
Escribe una funcion que sume pida al usuario numero1, numero2 y numero3.
Al numero 3 lo elevara al cuadrado y luego, sera sumado al numero1 y numero2
"""
# numero1 = int(input("Ingresa un numero: "))
# numero2 = int(input("Ingresa otro numero: "))
# numero3 = int(input("Ingresa un numero diferente: "))
# resultado = lambda numero1, numero2, numero3 : numero1 + numero2 + (numero3*numero3)
# print(resultado(numero1, numero2, numero3))

"""
EJERCICIO #5 - MAP
Estructura de la funcion MAP:
map(funcion_a_realizar, estructura_de_dato)

Realiza una funcion que pida un numero al usuario cuatro numeros
Los deberas meter a la lista llamada numeros
Luego, mediante map, pasale la siguiente lista como parametro, imprimiendo los resultados
numeros = [2,3,4,5]
"""
# numeros = []

# numero1 = int(input("Ingresa un numero: "))
# numero2 = int(input("Ingresa un numero: "))
# numero3 = int(input("Ingresa un numero: "))
# numero4 = int(input("Ingresa un numero: "))
# numeros.append(numero1)
# numeros.append(numero2)
# numeros.append(numero3)
# numeros.append(numero4)

# def cuadrado(numero):
#     return numero*numero

# resultado = list(map(cuadrado, numeros))
# print(resultado)

"""
EJERCICIO #6 - MAP y LAMBDA
Resuelve el problema anterior usando MAP y LAMBDA
"""
# print("###################################################")
# resultado = list(map(lambda numero: numero*numero, numeros))
# print(resultado)
