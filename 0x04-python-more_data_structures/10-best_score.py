#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = []
    valor = list(a_dictionary.values())
    nombre = list(a_dictionary.keys())
    best_key.append(nombre[valor.index(max(valor))]
    print(best_key[0])
    return best_key[0]
