# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:01:07 2023

@author: DIANA ZAMBRANO Y ANDRES FLORES
"""

print('__________________MODULO VALIDACIÓN_____________________')
print('\n valInt')
def valInt(numero, rango=None):
    # Verificar si el número es un entero
    if not isinstance(numero, int):
        return False

    # Verificar si el rango es válido
    if rango is not None:
        if not isinstance(rango, (list, tuple)) or len(rango) != 2:
            raise ValueError("El rango debe ser una lista o tupla de dos elementos.")

        if not all(isinstance(x, int) for x in rango):
            raise TypeError("Los elementos del rango deben ser enteros.")

        if rango[0] > rango[1]:
            raise ValueError("El rango debe estar ordenado de manera creciente.")

        if not rango[0] <= numero <= rango[1]:
            return False

    return True

#EJEMPLO:
print(valInt(4.0))
print(valInt(4))
print(valInt(4.4, (4.4, 10)))
print(valInt(4.4, (4, 10)))
print(valInt(4.1, [4.1, 9.05]))
print(valInt(4.2, [4, 10]))
print(valInt(4.4, [10, 4]))

print('\n valFloat')
def valFloat(num, interval=None):
    if isinstance(num, float):
        if interval is None:
            return True
        elif isinstance(interval, (tuple, list)) and len(interval) == 2 and interval[0] < interval[1]:
            if interval[0] <= num <= interval[1]:
                return True
            else:
                return False
        else:
            return ValueError("El intervalo no está ordenado de manera creciente o tiene un tamaño no considerado")
    else:
        return False
#EJEMPLO:
print(valFloat(4.0))
print(valFloat(4))
print(valFloat(4.4, (4.4, 10)))
print(valFloat(4.4, (4, 10)))
print(valFloat(4.1, [4.1, 9.05])) 
print(valFloat(4.2, [4, 10]))  
print(valFloat(4.4, [10, 4]))
print(valFloat(4, 5))
    
print('\n valComplex')
def valComplex(z, interval=None):
    if isinstance(z, complex):
        if interval is None:
            return True
        else:
            if not isinstance(interval, (list, tuple)) or len(interval) != 2:
                return ValueError("El segundo argumento debe ser una lista o tupla de dos elementos")
            a, b = interval
            if not all(isinstance(x, (int, float)) for x in (a, b)):
                raise TypeError("Los elementos de la lista o tupla deben ser números")
            if a > b:
                return ValueError("El intervalo debe estar ordenado de manera creciente")
            if abs(z) >= a and abs(z) <= b:
                return True
            else:
                return False
    else:
        return False
#EJEMPLO:
print(valComplex(3+4j))
print(valComplex(4.0))
print(valComplex(3+4j, (5,10)))
print(valComplex(3+4j, [5,10]))
print(valComplex(3+4j, [4,10]))
print(valComplex(3+4j, [10,4]))
print(valComplex(3+4j, 5))

print('\n valList')
def valList(arg1, arg2=None, arg3=None):
    if arg3 is not None:
        if not isinstance(arg2, list) or not isinstance(arg3, str):
            return TypeError("Los tipos de los argumentos 2 y 3 no son los esperados.")
        if arg3 not in ['len', 'value']:
            raise ValueError("El tercer argumento debe ser 'len' o 'value'.")
        if arg3 == 'len':
            return isinstance(arg1, list) and len(arg1) == arg2
        else:
            return isinstance(arg1, list) and arg1 == arg2
    else:
        if not isinstance(arg1, list):
            return False
        if arg2 is not None:
            return len(arg1) == arg2
        else:
            return True
#EJEMPLO:
print(valList(4.0, 2, 3))
print(valList(4.1, [4.1, 9.05], [2])) 
print(valList(4.2, [4, 10]))  
print(valList(4.4, [10, 4]))
print(valList([4], [5], [6]))
