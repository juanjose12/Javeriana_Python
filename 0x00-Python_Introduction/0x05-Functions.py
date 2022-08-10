#!/usr/bin/python3

def completeDivision(numerator,denominator):
    if(denominator==0):
        print("Error")
    else:
        print("Cociente", numerator//denominator)
        print("Residuo", numerator%denominator)

def sumar(a,b):
    print("Resultado de la suma: ",a+b)

def Restar(a,b):
    print("Resultado de la resta: ",a-b)

def multiplicar(a,b):
    print("Resultado de la multiplicacion: " , a*b)

def potenciar(a,b):
    print("Resultado de la potencia: ", a**b)


completeDivision(5,2)
sumar(3,8)
Restar(5,11)
multiplicar(4,8)
potenciar(5,2)
