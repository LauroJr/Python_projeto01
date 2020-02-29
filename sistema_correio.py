# Programa faz leitura para o correio.

valor = 1
n1 = 1
while (valor < 70) or (valor > 620) or (n1 != 0):
    valor = float(input())
    valor = (valor/10) *1000
    valor = round(valor, 0)
    r1 = valor//10
    r2 = valor/10
    n1 = r2-r1
    if valor < 70 or valor > 620 or n1 != 0:
        print("Preco invalido, refaça a leitura do pacote.")
    else:
        v1 = valor//50
        aux1 = v1*50
        aux2 = valor - aux1
        if aux2 == 10 or aux2 == 30:
            if aux2 == 10:
                total = valor - 60
                total = total // 50
                print("Compre {:.0f}".format(total),"selo(s) de R$ 0.50 e {:.0f}".format(3),"selo(s) de R$ 0.20!")
            else:
                k = valor - 80
                k = k//50
                t = 80/20
                print("Compre {:.0f}".format(k),"selo(s) de R$ 0.50 e {:.0f}".format(t),"selo(s) de R$ 0.20!")
        else:
            v2 = valor//50
            aux3 = v2*50
            aux4 = valor-aux3
            aux5 = aux4/20
            print("Compre {:.0f}".format(v2),"selo(s) de R$ 0.50 e {:.0f}".format(aux5),"selo(s) de R$ 0.20!")
