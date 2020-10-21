"""Dada uma tupla, retorne uma nova tupla com todos os elementos invertidos.
"""

def invertevalortupla():
    tupla = ()
    criatupla = input("Digite os elementos para criar sua tupla: ")
    tupla = criatupla
    print(tupla)
    lista_1 = list(tupla)
    lista_1.reverse()
    novatupla = tuple(lista_1)
    print(novatupla) 
invertevalortupla()