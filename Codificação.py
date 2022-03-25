# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

lista = [4,4,4,4,4,4,6,8,8,8,7]
repeticoes = []
atribuicoes = []
cod = []
cod_certo=[]

a = set(lista)
a = list(a)

for i in a:
    b = lista.count(i)
    repeticoes.append(b)
    
c = len(repeticoes)
mm = sorted(repeticoes, reverse = True)

# for i in range(c):
#     atribuicoes[a[i]] = repeticoes[i]

indice = 0
tamanho = len(a)

num = "0"
for i in range(tamanho):
    cod.append(num)
    num = num + "1"
    
for i in cod:
    i = i[::-1]
    cod_certo.append(i)
    
for i in range(c):
    atribuicoes.append(a[indice])
    atribuicoes.append(repeticoes[indice])
    indice = indice + 1

lista2 = []

for i in range(len(atribuicoes)):
    if (i%2) != 0:
        lista2.append(i)

def apagar():
    p = max(mm)
    indice2 = mm.index(p)
    mm.pop(indice2)
    return p

indice3 = 0
for i in atribuicoes:
    j = atribuicoes.index(apagar())-1
    atribuicoes[j] = int(cod_certo[indice3])
    indice3 = indice3 + 1