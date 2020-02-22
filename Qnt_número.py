def Quantidade_de_Caracter_Num(n1):
    totalCarac = 0
    for numero in n1:
        totalCarac += 1
    return(totalCarac)


n1 = input()
qnt = Quantidade_de_Caracter_Num(n1)
print(qnt)
