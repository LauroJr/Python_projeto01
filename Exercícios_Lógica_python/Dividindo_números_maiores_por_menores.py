n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
if n1 > n2:
    if n2 != 0:
        r= n1/n2
        print(r)
    else:
        print("Impossível dividir por 0")
else:
    if n1 != 0:
        r = n2/n1
        print(r)
    else:
        print("Impossível dividir por 0")
        
