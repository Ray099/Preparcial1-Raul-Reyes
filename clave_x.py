import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""

# start-->
def suma():
    x = int(2)
    y = int(4)
    return x + y


"""
***************************************************************
@@ ejercicio 2 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*5 = 40
"""


# start-->
def multiplicacion():
    x = int(2)
    y = int(4)
    z = int(5)
    return x*y*z


"""
***************************************************************
@@ ejercicio 3 @@
un metodo python que haga la suma de los numeros de la lista
numerosLista = [2,5,4,6,9,12]
"""


# start-->
def sumarLista():
    numeroLista = [2,5,4,6,9,12]
    sumaNumeros = 0
    for numeros in numeroLista:
        sumaNumeros += numeros
    return sumaNumeros

"""
***************************************************************
@@ ejercicio 4 @@
colocar este proyecto en github
colocar aca debajo la url
enviar la url al correo balbino_a@hotmail.com
"""


# github url-->
def getGithubUrl():
    url = str("https://github.com/Ray099/Preparcial1-Raul-Reyes.git")
    return url
