# ============================================
# Calculadora RPN (Notación Polaca Inversa)
# ============================================
"""
Este programa implementa una calculadora basada en notación polaca inversa (RPN).
Permite evaluar expresiones matemáticas utilizando una pila.

Soporta:
- Operaciones básicas (+, -, *, /)
- Funciones matemáticas (log, ln, sqrt, etc.)
- Funciones trigonométricas
- Manejo de memoria
- Manejo de errores personalizados
"""

import math
import sys


class RPNError(Exception):
    """Excepción personalizada para errores de la calculadora RPN."""
    pass


# ============================================
# FUNCIONES AUXILIARES
# ============================================

def validar_pila(pila, cantidad):
    """
    Verifica que la pila tenga la cantidad mínima de elementos requerida.
    """
    if len(pila) < cantidad:
        raise RPNError("Pila insuficiente")


def operar_binario(op, a, b):
    """
    Ejecuta operaciones binarias entre dos operandos.
    """
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b

    # División con control de error
    if op == "/":
        if b == 0:
            raise RPNError("División por cero")
        return a / b

    raise RPNError(f"Operación inválida: {op}")


def operar_unario(op, a):
    """
    Ejecuta operaciones matemáticas sobre un solo operando.
    """
    if op == "sqrt":
        if a < 0:
            raise RPNError("Raíz negativa")
        return math.sqrt(a)

    if op == "log":
        return math.log10(a)

    if op == "ln":
        return math.log(a)

    if op == "ex":
        return math.exp(a)

    if op == "10x":
        return 10 ** a

    if op == "1/x":
        if a == 0:
            raise RPNError("División por cero")
        return 1 / a

    if op == "chs":
        return -a

    raise RPNError(f"Operación inválida: {op}")


def operar_trig(op, a):
    """
    Ejecuta funciones trigonométricas (entrada en grados).
    """
    a = math.radians(a)

    if op == "sin":
        return math.sin(a)
    if op == "cos":
        return math.cos(a)
    if op == "tg":
        return math.tan(a)

    raise RPNError(f"Operación inválida: {op}")


def operar_trig_inv(op, a):
    """
    Ejecuta funciones trigonométricas inversas (resultado en grados).
    """
    if op == "asin":
        return math.degrees(math.asin(a))
    if op == "acos":
        return math.degrees(math.acos(a))
    if op == "atg":
        return math.degrees(math.atan(a))

    raise RPNError(f"Operación inválida: {op}")


# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def eval_rpn(tokens):
    """
    Evalúa una expresión en notación RPN utilizando una pila.
    """
    pila = []
    memoria = {f"{i:02}": 0.0 for i in range(10)}

    for token in tokens:

        # ----------------------------------------
        # Intentar convertir el token a número
        # ----------------------------------------
        try:
            pila.append(float(token))
            continue
        except ValueError:
            pass

        # ----------------------------------------
        # Constantes matemáticas
        # ----------------------------------------
        if token == "p":
            pila.append(math.pi)
            continue

        if token == "e":
            pila.append(math.e)
            continue

        if token == "j":
            pila.append((1 + math.sqrt(5)) / 2)
            continue

        # ----------------------------------------
        # Operaciones binarias
        # ----------------------------------------
        if token in "+-*/":
            validar_pila(pila, 2)
            b = pila.pop()
            a = pila.pop()
            pila.append(operar_binario(token, a, b))
            continue

        # ----------------------------------------
        # Operaciones de pila
        # ----------------------------------------
        if token == "dup":
            validar_pila(pila, 1)
            pila.append(pila[-1])
            continue

        if token == "swap":
            validar_pila(pila, 2)
            pila[-1], pila[-2] = pila[-2], pila[-1]
            continue

        if token == "drop":
            validar_pila(pila, 1)
            pila.pop()
            continue

        if token == "clear":
            pila.clear()
            continue

        # ----------------------------------------
        # Operaciones unarias
        # ----------------------------------------
        if token in {"sqrt", "log", "ln", "ex", "10x", "1/x", "chs"}:
            validar_pila(pila, 1)
            pila.append(operar_unario(token, pila.pop()))
            continue

        # ----------------------------------------
        # Potencia
        # ----------------------------------------
        if token == "yx":
            validar_pila(pila, 2)
            b = pila.pop()
            a = pila.pop()
            pila.append(a ** b)
            continue

        # ----------------------------------------
        # Trigonometría
        # ----------------------------------------
        if token in {"sin", "cos", "tg"}:
            validar_pila(pila, 1)
            pila.append(operar_trig(token, pila.pop()))
            continue

        if token in {"asin", "acos", "atg"}:
            validar_pila(pila, 1)
            pila.append(operar_trig_inv(token, pila.pop()))
            continue

        # ----------------------------------------
        # Manejo de memoria
        # ----------------------------------------
        if token.startswith("STO"):
            k = token[3:]
            if k not in memoria:
                raise RPNError("Memoria inválida")
            validar_pila(pila, 1)
            memoria[k] = pila[-1]
            continue

        if token.startswith("RCL"):
            k = token[3:]
            if k not in memoria:
                raise RPNError("Memoria inválida")
            pila.append(memoria[k])
            continue

        # ----------------------------------------
        # Token inválido
        # ----------------------------------------
        raise RPNError(f"Token inválido: {token}")

    # ----------------------------------------
    # Validación final del resultado
    # ----------------------------------------
    if len(pila) != 1:
        raise RPNError("Resultado inválido")

    return pila[0]


# ============================================
# FUNCIÓN MAIN
# ============================================

def main():
    """
    Punto de entrada del programa.
    Permite ingresar datos por consola o input.
    """
    try:
        tokens = sys.argv[1:] if len(sys.argv) > 1 else input().split()
        print(eval_rpn(tokens))
    except RPNError as e:
        print("Error:", e)


# ============================================
# EJECUCIÓN
# ============================================

if __name__ == "__main__":
    main()