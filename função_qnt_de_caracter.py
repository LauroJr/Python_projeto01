def Quantidade_de_Caracter(msg):
    totalCarac = 0
    for letra in msg:
        totalCarac += 1
    return(totalCarac)


msg = input()
qnt = Quantidade_de_Caracter(msg)
print(qnt)
