#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                        *
#* calcula el factorial de un número usando POO                            *
#*-------------------------------------------------------------------------*

import sys

class Factorial:

    # Constructor
    def __init__(self):
        pass

    # Método para calcular factorial
    def factorial(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    # Método principal requerido por la consigna
    def run(self, desde, hasta):
        for i in range(desde, hasta + 1):
            print("Factorial", i, "! es", self.factorial(i))


# -------------------- MAIN --------------------

# Si se pasa argumento por consola
if len(sys.argv) > 1:
    entrada = sys.argv[1]
else:
    # Si no, pedir por teclado
    entrada = input("Ingrese un número o rango: ")

# Procesamiento de la entrada
if "-" in entrada:
    partes = entrada.split("-")

    # Caso "-hasta" (ej: -10)
    if partes[0] == "":
        desde = 1
        hasta = int(partes[1])

    # Caso "desde-" (ej: 4-)
    elif partes[1] == "":
        desde = int(partes[0])
        hasta = 60

    # Caso "desde-hasta" (ej: 4-8)
    else:
        desde = int(partes[0])
        hasta = int(partes[1])

else:
    desde = int(entrada)
    hasta = int(entrada)

# Crear objeto y ejecutar
f = Factorial()
f.run(desde, hasta)
