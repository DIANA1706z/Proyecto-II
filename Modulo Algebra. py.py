# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:24:27 2023

@author: DIANA ZAMBRANO
"""

print('______________MODULO ÁLGEBRA_________________')

from random import randint #Para generar numeros aleatorios.
import numpy as np #Para que me imprima la matriz como una lista de listas

print('\nGENERAR MATRIZ:')
def create_matriz(M, N):
    matriz = []    
    for i in range(1, M+1):
        fila = []       
        for j in range(1, N+1):
            fila.append(randint(1, N+1))            
        matriz.append(fila)            
    return matriz        
M = int(input('Ingrese el número de filas que desea en su primera matriz: '))
N = int(input('Ingrese el número de columnas que desea en su primera matriz: '))
M_1 = int(input('Ingrese el número de filas que desea en su primera matriz: '))
N_1 = int(input('Ingrese el número de columnas que desea en su primera matriz: '))
result = create_matriz(M, N)
result_m = create_matriz(M_1, N_1)
matriz_1 = np.array(result)
matriz_4 = np.array(result_m)
print('Esta es su primera matriz:\n', matriz_1)
print('Esta es su seguda matriz:\n', matriz_4)

print('\nMATRIZ TRASPUESTA')
def trasponer(matriz_1) :
    matriz_t = []    
    for i in range(len(matriz_1[0])):
        matriz_t.append([])       
        for j in range(len(matriz_1)):
            matriz_t[i].append(matriz_1[j][i])
    return matriz_t
traspuesta = trasponer(matriz_1)
result_traspuesta = np.array(traspuesta)
print('\nLa traspuesta de su primera matriz es:\n', result_traspuesta)

print('\nSUMA DE MATRICES')
def suma_matriz(matriz_1, matriz_4) :
    result_matriz = []   
    if M != M_1 and N != N_1 :
        print('Las matrices no son de igual dimensión')
    if M == M_1 and N == N_1 :
        suma_matriz = matriz_1 + matriz_4   
        result_matriz.append(suma_matriz)
        return result_matriz
    else:
        return None
        if result_2 == None:
            print('No se puede ejecutar la operación.')
result_2 = suma_matriz(matriz_1, matriz_4)
matriz = np.array(result_2)
print('El resultado de la suma de las matrices formadas es:\n', matriz)

print('\nMULTIPLICACIÓN DE MATRICES')
def multiplicar_matriz(matriz_1, matriz_4) :
    result_multiplication = []
    if M == N_1 :
        for i in range(len(matriz_1)) :
            result_multiplication.append([])
            for j in range(len(matriz_4[0])) :
                result_multiplication[i].append(0)
        
        for i in range(len(matriz_1)) : 
            for j in range(len(matriz_4[0])):
                for r in range(len(matriz_1[0])):
                    result_multiplication[i][j] += matriz_1[i][r] * matriz_4[r][j]
        return result_multiplication
    else:
        return None
        if result_3 == None :
            print('No se puede ejecutar la operación.')
result_3 = multiplicar_matriz(matriz_1, matriz_4)
matriz_rm = np.array(result_3)
print('El resultado de la multiplicación de las matrices formadas es:\n', matriz_rm)

print('\nSISTEMA DE ECUACIONES , DETERMINANTE')
matriz = []
res = []

def mat(n):
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    return matriz

def llenar_matriz(n):
    matriz = mat(n)
    for x in range(n):
        for y in range(n):
            matriz[x][y] = int(input('Valor de coeficiente de la ecuación [' + str(x) + '][' + str(y) + '][' + str(x) + ']:\n'))
        res.append(int(input('Valor de la constante de la ecuación [' + str(x) + ']:\n')))                       
def gauss(n) :
    for z in range(n-1) :
        for x in range(1,n-z) :
            if  matriz[z][z] != 0 :
                p = matriz[x+z][z] / matriz[z][z]
                for y in range(n) :
                    matriz[x+z][y] = matriz[x+z][y] - (matriz[z][y]*p)
                    res[x+z] = res[x+z] - (res[z]*p)
def gauss_jordan(n):
    for z in range(n-1, 0, -1) :
        for x in range(z) :
            if matriz[z][z] != 0 :
                p = matriz[x][z] / matriz[z][z]
                matriz[x][z] = matriz[x][z] - (matriz[z][z]*p) 
                res[x] = res[x] - (res[z]*p)

def sol(n):
    print('\n')
    for i in range(n):
        if matriz[i][i] != 0 :
            ms = True
        else:
            ms = False
            break
    if ms == True:
        for i in range(n):
            print('El valor de x' + str(i) + 'es:' + str(res[i] / matriz[i][i]))
    else:
        print('La matriz no tiene solución')

def determinante(n):
    determinante = 1
    for x in range(n) :
        determinante = matriz[x][x]*determinante
    print('El determinante de la matriz es:\n', determinante)
    
n = int(input('Dimensión de la matriz:\n'))
llenar_matriz(n)
gauss(n)
gauss_jordan(n)
sol(n)
determinante(n)

print('\nPRODUCTO VECTORIAL')
def producto_vectorial(u, v):
    if len(u) != 3 or len(v) != 3:
        raise ValueError("Los vectores deben tener tres componentes")
    x = u[1]*v[2] - u[2]*v[1]
    y = u[2]*v[0] - u[0]*v[2]
    z = u[0]*v[1] - u[1]*v[0]
    return [x, y, z]

u = [1, 2, 3]
v = [4, 5, 6]
w = producto_vectorial(u, v)
print('Los vectores ejemplos para el producto vectorial son:', u,v, '\nEl resultado es:',w)

print('\nInversion Gauss Jordan')
def gauss_jordan(m):
    # Obtener el número de filas y columnas de la matriz
    n = len(m)
    c = len(m[0])
    # Añadir la matriz identidad a la derecha de la matriz original
    for i in range(n):
        m[i] += [1.0 if j == i else 0.0 for j in range(n)]
    # Iterar sobre las filas
    for i in range(n):
        # Buscar la fila con el valor máximo en la columna i
        max_row = i
        for j in range(i+1, n):
            if abs(m[j][i]) > abs(m[max_row][i]):
                max_row = j
        # Intercambiar la fila actual con la fila con el valor máximo en la columna i
        m[i], m[max_row] = m[max_row], m[i]
        # Dividir la fila actual por el valor en la columna i
        pivot = m[i][i]
        if pivot == 0:
            return None
        for j in range(i, c):
            m[i][j] /= pivot
        # Restar múltiplos de la fila actual de las filas restantes para hacer ceros en la columna i
        for j in range(n):
            if j != i:
                factor = m[j][i]
                for k in range(i, c):
                    m[j][k] -= factor * m[i][k]
    # Extraer la matriz inversa de la matriz extendida
    inverse = [row[c:] for row in m]
    return inverse
#EJEMPLO
m = [[2, 1, 1], [4, -6, 0], [-2, 7, 2]]
inverse = gauss_jordan(m)
if inverse is not None:
    for row in inverse:
        print(row)
else:
    print("La matriz no tiene inversa")
