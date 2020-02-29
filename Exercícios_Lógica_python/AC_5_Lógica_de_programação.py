''' Este programa calcula média, diferença do maior pelo menor,
    e multiplicação.
'''

p = 0
while p >= 0:
    n1 = int(input())
    n2 = int(input())
    print("[1] Média entre os números digitados: ")
    print("[2] Diferença do maior pelo menor: ")
    print("[3] Produto entre os números digitados: ")
    p = int(input("opção: "))
    if p == 1:
        m = (n1+n2)/2
        print(m)
    else:
        if p == 2:
            if n1 > n2:
                t = n1-n2
                print(t)
            else:
                t = n2-n1
                print(t)
        else:
            if p == 3:
                 L = n1*n2
                 print(L)
            else:
                 print("Opção nº",p,"Não existe. Por favor escolher entre as opções de 1 á 3")
        
                 
