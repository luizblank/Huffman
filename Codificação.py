# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

lista = [4,4,4,4,4,4,6,8,8,8,7]
repeticoes = []
atribuicoes = []

a = set(lista)
a = list(a)

for i in a:
    b = lista.count(i)
    repeticoes.append(b)
    
c = len(repeticoes)

# for i in range(c):
#     atribuicoes[a[i]] = repeticoes[i]

indice = 0
    
for i in range(c):
    atribuicoes.append(a[indice])
    atribuicoes.append(repeticoes[indice])
    indice = indice + 1

for i in range(len(atribuicoes)):
    if (i%2) != 0:
        print(bin(atribuicoes[i]))