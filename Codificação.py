# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

lista = [7,7,7,3,6,2,2,2,2,2,2,5,5,5,4,9,8,1]
repeticoes = []
atribuicoes = []
atribuicoes1 = []
cod = []
cod_certo=[]
lista_correta = []

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
    atribuicoes1.append(a[indice])
    atribuicoes1.append(repeticoes[indice])
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

tamanho1 = len(atribuicoes)
indice3 = 0
for i in mm:
    j = atribuicoes.index(apagar())
    z = atribuicoes[j]
    x = int(cod_certo[indice3])
    indice3 = indice3 + 1
    lista_correta.append(x)
    lista_correta.append(z)
    atribuicoes.pop(j)
    atribuicoes.pop(j-1)
    
print(lista_correta)