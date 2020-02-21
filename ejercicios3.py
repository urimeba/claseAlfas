
"""
EJERCICIO #1
Funcion que pida un monto en dinero, decimal o no, y que devuelva el
 monto mas el 16 de IVA
"""
#value = int(input("Ingrese un monto"))
#monto = (value * .16)
#print(str(value + monto))


"""
EJERCICIO #2
Funcion que pida tres numeros y encuentre el mayor
"""

   # def Mayor(a, b, c):
   #     mayor = 0
   #     if(a >= mayor):
   #         mayor = a
   #     if(b >= mayor):
   #         mayor = b
   #     if(c >= mayor):
   #         mayor = c
   #     print(mayor)
   # Mayor(20,50,30)
"""
EJERCICIO #3
Funcion que pida N numeros y los multiplique todos
"""
#def devolver(a,b):
#    return a * b
#
#numeros = int(input("que tan grande"))
#lista = []
#
#for num in range(0,numeros):
#    lista.append(int(input(":")))
#
#multiplicados = devolver(1,lista[0])
#for num in range(0,numeros):
#    num += 1
#    try:
#        multiplicados = devolver(multiplicados,lista[num])
#    except IndexError:
#        break
#print(multiplicados)

# def multiplicador (*args):
#     total = 1
#     for arg in args:
#         total = total * arg
#     return total
# 
# print(multiplicador(1,2,3,4))

"""
EJERCICIO #4
Funcion que calcule el factorial de un numero
"""
#numero = int(input("Ingrese un numero: "))
#def factorial(numero):
#          var = 1
#          for num in range (1, numero):
#          var = (num*var)
#          return var
#
#print(factorial(numero))
#
"""
EJERCICIO #5
Pide un string y debera imprimirse en orden reverso
ejemplo: "Uriel se encuentra ocupado"
Salida: "ocupado encuentra se Uriel"
"""

def Reversa(Text):
    palabras = Text.split(' ')
    palabra = ""
    for i in palabras[::-1]:
        palabra += i + " "
    print(palabra)

texto = input("Ingresa el String : ")

Reversa(texto)