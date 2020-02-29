''' Este programa foi feito para analisar o pacote de envio. Tem por objetivo analisar
    se o mesmo est'` dentro dos parâmetros permitido para envio
'''

peso = 0
alt = 0
lado = 0
cumpr = 0
while peso < 1:
    peso = float(input())
    if peso < 1:
        print("Peso invalido!")
    else:
        print("Peso Valido")
while ((alt < 1) or (lado < 1) or (cumpr < 1)):
       alt = float(input())
       lado = float(input())
       cumpr = float(input())
       if ((alt < 1) or (lado < 1) or (cumpr < 1)):
           print("Dimensoes invalidas")
       else:
           print("Dimensoes validas")
s = alt+lado+cumpr
if (alt > 0 and alt <= 28) and (lado > 0 and lado <= 28) and (cumpr > 0 and cumpr <=28) and (s <= 52) and (peso <= 500):
    C_peso = 0.50+(((peso-100)//10)/10)
    if s <= 22:
        C_dimen = 0.20
    else:
        C_dimen = 0.20+(((s-22)//2)/10)
    total = C_peso + C_dimen
    print("Custo total do envio: R${:.2f}".format(total))
else:
    print("Este pacote nao atende os limites para envio no caixa de autoatendimento, dirija-se ao balcao de atendimento para posta-lo")    
     
    
    
    
