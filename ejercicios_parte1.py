# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:40:22 2024

@author: Olivia Lorente Casalini

Ejercicios día 1 - Parte 1
"""

# 1.- Crea una lista de 10 elementos, que contenga al menos una variable entera, 
# una flotante, una booleana, una cadena de texto (holamundo), y una lista de al
# menos 3 números. Indica además el tamaño de la lista por pantalla.

lista = [1, 2.2, True, "holamundo", [1, 2, 3], "esto", "es", "un", "ejercicio", 10]

#%% 
# 2.- Visualiza el primer elemento de la lista.

lista[1]

#%% 
# 3.- Visualiza los elementos intercalados de dos en dos empezando por el tercero.

lista[2:9:2]

#%% 
# 4.- Suma los elementos numéricos de la lista que has creado. 
# Asigna el resultado a una variable que se llame F, e imprímela por pantalla.

F = lista[0] + lista[1] + lista[9]
print(F)

#%% 
# 5.- Visualiza el tipo de variable F.

type(F)

#%% 
# 6.-Separa la cadena de texto en dos cadenas asignándosela a dos variables distintas.

lista[3]

a = lista[3][0:4] 
b = lista[3][4:]

"""
Lo que le está diciendo es lo siguiente: de la posición cuarta, que es una cadena de texto,
crea el objeto a con los primeros 4 elementos de esa cadena y el b, con los siguientes a 
partir del cuarto
"""

#%% 
# 7.- Junta las cadenas en una misma variable.

c = a + b

#%% 
# 8.- Mediante operadores booleanos deduce si el primer valor de la lista es mayor, 
# menor o igual al segundo

lista[0] == lista[1]

lista[0] > lista[1]

lista[0] < lista[1]

#%% 
# 9. Mediante operadores lógicos comprueba si el tercer elemento de la sublista de números 
# y el elemento decimo de la lista son iguales a 9.

lista[4][2] and lista[9] == 9

#%% 
# 10. Modifica el elemento decimo de la lista para que valga 9 y repite el apartado 9.

lista[9] = 9
print(lista)

lista[4][2] and lista[9] == 9

#%% 
# 11. Crea un programa con el editor de código que permita:

# indicar el tamaño que queremos que tenga el diccionario,

# crear un diccionario vacío,

# rellenar uno a uno las clave y valor de los elementos. El valor será una lista del tamaño 
# que le indiquemos previamente.

# cada elemento tendrá como clave un DNI y como valores los que le queramos introducir, 
# pudiendo ser variable en cada elemento de acuerdo al tamaño indicado 
# (por ejemplo: nombre, apellidos; nombre, apellidos, teléfono)

size = int(input("Indica el tamaño del diccionario"))

diccionario = {}

for i in range(0,size):
    
    clave = input("Introduce la nueva clave")
    long_lista_valor = int(input("Cuantos datos va a tener la clave{}".format(clave)))
    lista = []
    for j in range(0,long_lista_valor):
        lista.append(input("Introduce un nuevo valor para la lista de la clave{}".format(clave)))
    diccionario[clave] = lista

print(diccionario)








