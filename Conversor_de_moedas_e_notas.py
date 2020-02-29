''' Este código tem por objetivo receber um valor Float em Reais, e mostrar ao
    usuário quantos notas de 100, 50, 20, 10, 5, 2, e moedas de 50, 25, 10, 5, 1
    serão necessárias.
'''

d = float(input())
d = round(d, 2)
if d > 0:
    qnt1 = d//100         ## apartir desta  linha até a linha da váriavel r7, é o conversor dos reais
    r1 = d-(qnt1*100)
    r1 = round(r1, 2)
    qnt2 = r1//50
    r2 = r1-(qnt2*50)
    r2 = round(r2, 2)
    qnt3 = r2//20
    r3 = r2-(qnt3*20)
    r3 = round(r3, 2)
    qnt4 = r3//10
    r4 = r3-(qnt4*10)
    r4 = round(r4, 2)
    qnt5 = r4//5
    r5 = r4-(qnt5*5)
    r5 = round(r5, 2)
    qnt6 = r5//2
    r6 = r5-(qnt6*2)
    r6 = round(r6, 2)
    qnt7 = r6//1
    r7 = r6-(qnt7*1)
    r7 = round(r7, 2)
    r7 = r7*100
    cent1 = r7//50     ###
    s1 = r7-(cent1*50) #
    cent2 = s1//25     #
    s2 = s1-(cent2*25) # Neste trecho se encontra o conversor dos centavos. Eu converti os centavos( números reais), para número inteiros para facilitar a conversão
    cent3 = s2//10     #
    s3 = s2-(cent3*10) #
    cent4 = s3//5      ###
    s4 = s3-(cent4*5)
    cent5 = s4/1       
if qnt1 > 0:     
    print("{:.0f}".format(qnt1)," nota(s) de R$ 100.00")
if qnt2 > 0:
    print("{:.0f}".format(qnt2)," nota(s) de R$ 50.00")
if qnt3 > 0:
    print("{:.0f}".format(qnt3)," nota(s) de R$ 20.00")
if qnt4 > 0:
    print("{:.0f}".format(qnt4)," nota(s) de R$ 10.00")
if qnt5 > 0:
    print("{:.0f}".format(qnt5)," nota(s) de R$ 5.00")
if qnt6 > 0:
    print("{:.0f}".format(qnt6)," nota(s) de R$ 2.00")
if qnt7 > 0:
    print("{:.0f}".format(qnt7)," moeda(s) de R$ 1.00")
if cent1 > 0:
    print("{:.0f}".format(cent1)," moeda(s) de R$ 0.50")
if cent2 > 0:
    print("{:.0f}".format(cent2)," moeda(s) de R$ 0.25")
if cent3 > 0:
    print("{:.0f}".format(cent3)," moeda(s) de R$ 0.10")
if cent4 > 0:
    print("{:.0f}".format(cent4)," moeda(s) de R$ 0.05")
if cent5 > 0:
    print("{:.0f}".format(cent5)," moeda(s) de R$ 0.01")
    


































    
