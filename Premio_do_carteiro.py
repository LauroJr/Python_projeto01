'''Luíz Carlos é um carteiro muito comprometido com seu trabalho. Ele participou
    de uma reunião recente em que foi informado de que deveria entregar pelo menos 100 
    correspondências por dia para dar conta do grande fluxo de envios na época de Natal.
    Escreva um programa que receba como entrada a quantidade de correspondências 
    entregues por ele em cada um dos sete dias da semana, e exiba em quantos dias ele
    cumpriu a meta, e a média de entregas diárias que ele fez no período.
'''

cont = 1
soma = 0
dias = 0
while cont <= 7:
    qnt = int(input())
    soma = soma + qnt
    cont = cont+1
    if qnt >= 100:
        dias = dias+1
m = soma/7        
print(dias)
print("{:.0f}".format(m))
        
