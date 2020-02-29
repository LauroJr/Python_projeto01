 # este código tem por objetivo mostrar ao usuário o resultado das tábuadas
 #  conforme o próprio usuário irá escolher.
 # Por EX: Se o usuário digitar 1 e 5, então será exibido a tábuada do 1 até o 5.
 #  Se forem 3 e 8, serão exibidas do 3 ao 8.
 # Os números válidos devem estar apartir do 1 até o 9



valor1 = 0
valor2 = 10
cont = 1
print("")
print("====================================================================================================")
print("|     Digite dois valores para obter o resultado de suas respectivas tábuadas em seu intervalo     |")
print("====================================================================================================")
print("")
while valor1 < 1 or valor1 > 9:
    valor1 = int(input("Digite o primeiro número: "))
    if valor1 < 1 or valor1 > 9:
        print("Insira um número inicial entre 1 e 9")
while valor2 <1 or valor2 > 9:        
    valor2 = int(input("Insira o segundo número: "))    
    if valor2 > 9:
        print("Insira um número final entre 1 e 9")
if (valor1 > valor2):
    print("Nenhuma tabuada nesse intervalo")
if valor1 == valor2:
    while cont < 10:
        r1 = valor1*cont
        print(valor1,"x",cont,"=",r1)
        cont = cont+1
if valor1 > 0 and valor1 < 10 and valor2 > 0 and valor2 <=10 :
    while valor1 < valor2:
        while cont <= 9:
            r=valor1*cont
            print(valor1,"x",cont,"=",r)
            cont = cont+1
            if cont > 9 and valor1 < valor2:
                print("")
                cont = cont-9
                valor1 = valor1 + 1


                
