c = 0
n = 0
s = 0
ms = 0
while c <= 9:
    print("========================================================")
    print("Você gostou ou não do novo produto lançado no mercado?: ")
    resp = input("Sim / Não? [S/N]: ")
    sex = input("Qual seu sexo? [F/M]: ")
    if resp == 's':
        s = s+1
        if sex == 'f':
            ms = ms+1
    else:
        n = n+1
    c = c+1
print("=========================================")    
print(s," pessoa(s) responderam SIM")
print(n," pessoa(s) responderam NÃO")
print(ms," mulher(es) responderam SIM á pesquisa")
