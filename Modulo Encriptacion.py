# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:13:26 2023

@author: DIANA ZAMBRANO Y ANDRES FLORES
"""

print('___________________MODULO ENCRIPTACIÓN_____________________')

str_1= "Hola Martha ¿como estas? María"


def encriptar (str_1):
  str_1= str_1.lower()
  chars_x= "abc defghijklmnñopqrstuvwxyz0123456789!#$%&\/()=?¡¿.,áéíóú-"
  chars_y= "qwe rtyuioplñkjhgfdsazxcváéíóúbnm9\512364780,.-!#¿?=)(/&%$¡"

  str_1_encripted=""

  for i in str_1:
    for n in range (len(chars_x)):
      if i == chars_x [n]:
        str_1_encripted += chars_y[n]
  return str_1_encripted


str_1_cifrado = encriptar (str_1)

print (str_1_cifrado)

str_1= "igñq kqsziq (egkg tazqa= kqs¡q"


def desencriptar (str_1):
  str_1= str_1.lower()
  chars_y= "abc defghijklmnñopqrstuvwxyz0123456789!#$%&\/()=?¡¿.,áéíóú-"
  chars_x= "qwe rtyuioplñkjhgfdsazxcváéíóúbnm9\512364780,.-!#¿?=)(/&%$¡"

  str_1_encripted=""

  for i in str_1:
    for n in range (len(chars_x)):
      if i == chars_x [n]:
        str_1_encripted += chars_y[n]
  return str_1_encripted


str_1_cifrado = desencriptar (str_1)

print (str_1_cifrado)