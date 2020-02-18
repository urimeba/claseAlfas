"""
Estructura de una funcion en Python:
def nombre_funcion(argumento1, argumento2, n_argumento):
    realiza_alguna_operacion
    o_imprime_algo
    o regresa algun valor con
    return argumento1 + argumento2
"""

""" ¡NOTA LA IDENTACION! """
def saludo(nombre):
    return "Hola " + nombre + "!! Bienvenido!"

saludo("Uriel")





def suma(numero1, numero2):
    print( numero1 + numero2)

suma(1,2)





def resta(a, b):
    return a - b


#Que pasa si hago esto?
# resta()

# que pasa si no paso valores?

resta(5,1)
resta(b=5, a=1)












# POR POSICION
def posicional(*args):
    for arg in args:
        print (arg)
posicional(1,"Argumento posicional #2",[3,3,3,3])




# POR NOMBRE, O KEYWORD ARGS
def nombre(**kwargs):
    # print(kwargs)

    for kwarg in kwargs:
        print (kwarg, "=>", kwargs[kwarg])

nombre(n=1, c="Argumento C", l=[555,'asdas'])






# COMBINANDO AMBOS
def combinacional(*args,**kwargs):
    suma = 0
    for arg in args:
        suma += arg

    print ("Suma => ", suma)
    
    for kwarg in kwargs:
        print (kwarg, "=>", kwargs[kwarg])

combinacional(50, -1, 1.56, 10, 20, 300, cms="23.2", edad=38)





# FUNCION PASS

def saludar():
    pass
saludar()


# Retornando multiples valores
def multiple_retorno():
    return "Hola", 24, "Adios"

print(multiple_retorno())

saludo, edad, despedida = multiple_retorno()
print(saludo + ". Soy Uriel y tengo " + str(edad) + " años. " + despedida)

