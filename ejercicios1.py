"""
Ingresa a la documentacion oficial de Python actual y revisa algunas excepciones o errores
https://docs.python.org/3/library/exceptions.html#bltin-exceptions
Ejemplos: Exception, ArithmeticError, BufferError, LookupError
"""

"""
EJERCICIO #1 (TRY CATCH SI LA EDAD NO ES NUMERO)
Crea un programa que pida el nombre y la edad del usuario.
El programa debera imprimir en que año el usuario cumplira 100 años
"""
# nombre = input("Nombre: ")
# edad = int(input("Edad: "))

# edad_cien_anios = (2020 - edad) + 100
# print(nombre + " en " + str(edad_cien_anios) + " cumpliras 100 años")

"""
EJERCICIO #2 (TRY CATCH SI EL NUMERO NO ES POSITIVO)
Crea un programa que pida un numero entero positivo y le haga saber al usuario si es par o primo
(PISTA: investiga el operador modulo, denotado como % en muchos lenguajes de programacion)
"""

# numero = int(input("Ingresa un numero: "))

# if(numero%2==0):
#     print("Es par")
# else:
#     print("Es impar")



"""
EJERCICIO #3 
Tome estas listas: 
a = [1, 7, 22, 90, 32, 2, 92, 85, 12]
b = [1, 5, 77, 22, 90, 25, 83, 100, 02, 21, 90]
y crea un programa que cree una nueva lista (o array)
que contenga los elementos que NO se encuentran repetidos en ninguna de las dos lista anteriores
y se imprima la lista completa (tambien se puede imprimir cada elemento de la lista)
"""

# a = [1, 7, 22, 90, 32, 2, 92, 85, 12]
# b = [1, 5, 77, 22, 90, 25, 83, 100, 2, 21, 90]
# c = []
# d = len(b)
# e = len(a)
# for i in a : 
#     contador = 0
#     for x in b :
#         contador += 1 
#         if x==i :
#             break
#         if contador == d-1 : 
#             c.append(i)

# for i in b : 
#     contador = 0
#     for x in a :
#         contador += 1 
#         if x==i :
#             break
#         if contador == e-1:
#             c.append(i)
# print(c)






"""
EJERCICIO #4
Crea un programa que le pida al usuario una palabra y muestre si esa palabra es un palindromo
NOTA: un palindromo es una palabra que se puede escribir al derecho y al reves de la misma manera.
(Por ejemplo: ana, ala, oso)
(EXTRA: intenta hacerlo en 4 lineas de codigo solamente (investiga IF TERNARIO en Python))
"""
# word = input("Ingresa una palabra:\n")
# wordl = list(word)
# print("Es palindromo") if wordl == list(reversed(wordl)) else print("No es palindromo")

"""
EJERCICIO #5 (TRY CATCH SI EL ELEMENTO EN EL DICCIONARIO NO EXISTE)
Crea un programa con un diccionario que contenga de llave un nombre
y de valor el cumpleaños de esta persona.
El programa pedira el nombre de la persona y se debera imprimir la fecha de su cumpleaños
# """
# diccionario = {'Uriel':'02/07/1996', 'Ana':'08/07/2000', 'Jorge':'01/01/2001'}
# nombre = input("Ingresa el nombre de una persona: ")
# print(diccionario[nombre])

# # Agregando elementos a un diccionario
# diccionario["Fernando"] = "29/03/2000"

# nombre = input("Ingresa el nombre de una persona: ")
# print(diccionario[nombre])

# # Sobreescribiedo elementos de un diccionario. Ahora, Fernando nacio en el 2001
# diccionario["Fernando"] = "02/02/2001"

# nombre = input("Ingresa el nombre de una persona: ")
# print(diccionario[nombre])

# # Eliminando elementos de un diccionario. En este caso, eliminamos a Fernando
# del diccionario['Fernando']

# nombre = input("Ingresa el nombre de una persona: ")
# print(diccionario[nombre])

