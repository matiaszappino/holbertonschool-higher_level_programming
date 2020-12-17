#!/usr/bin/python3
def roman_to_int(roman_string):
    valor = 0
    suma = 0
    contador = 0
    contadorunos = 0
    largo = len(roman_string)
    for i in range(len(roman_string)):
        if roman_string[i] != "I":
            if roman_string[i] == "X":
                valor = 10
                suma += valor
            if roman_string[i] == "V":
                valor = 5
                suma += valor
            if roman_string[i] == "L":
                valor = 50
                suma += valor
            if roman_string[i] == "C":
                valor = 100
                suma += valor
            if roman_string[i] == "D":
                valor = 500
                suma += valor
            if roman_string[i] == "M":
                valor = 1000
                suma += valor
            if contadorunos > 0:
                suma += -contadorunos
            contador = contador + 1
        else:
            valor = 1
            suma += valor
            contadorunos = contadorunos + 1
    return suma
