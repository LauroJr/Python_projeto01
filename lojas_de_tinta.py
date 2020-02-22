'''
Imagine que você fora contratado para fazer um programa para uma loja de tintas, com o objetivo de calcular
quantas latas de tinta são necessárias para pintar uma determinada área e calcular o preço final da compra.

A loja trabalha com latas de tinta de:
24 litros, vendidas a R$91,00 cada e,
5.4 litros, vendidas a R$23,00 cada.
Sabe-se ainda que cada litro de tinta cobre uma superfície de 7 metros quadrados.

Faça um programa que receba o valor da área a ser pintada em metros quadrados, calcule e imprima:

a) A quantidade de latas de tinta e o preço final, considerando apenas latas de 24 litros.
b) A quantidade de latas de tinta e o preço final, considerando apenas latas de 5.4 litros.
c) A quantidade de latas de tinta e o preço final, considerando ambas as latas, de 24 e 5.4 litros.
'''

import math
print("AC 2 PYTHON EXERCÍCIO 2")
a = float(input())
lts = a/7
lts = math.ceil(lts)
l = lts/24
L1 = math.ceil(l)
l2 = lts/5.4
L2 = math.ceil(l2)
L3 = math.floor(l)
f = (a/7) - L3*24
l3 = f/5.4
L4 = math.ceil(l3)
preço1 = L1*91.00
preço2 = L2*23.00
preço3 = L3*91.00
preço4 = L4*23.00
total = preço3 + preço4 
qt1 = 24.00
qt2 = 5.4
print("a)",L1,"lata(s) de {:.0f}".format(qt1),"litros: R$ {:.2f}".format(preço1))
print("b)",L2,"lata(s) de",qt2,"litros: R$ {:.2f}".format(preço2))
print("c)",L3,"lata(s) de {:.0f}".format(qt1),"litros e",L4,"lata(s) de",qt2,"litros: R$ {:.2f}".format(total))

