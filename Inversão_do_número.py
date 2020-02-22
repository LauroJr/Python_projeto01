n1 = (int(input("Escreva um número inteiro com 3 dígitos: ")))
n2 = n1 // 100
n3 = n2 * 100
n4 = n1 - n3
n5 = n4 // 10
n6 = n4 % 10
a = (n2*1) + (n5*10) + (n6*100)
print("O valor ",n1," INVERTIDO é: ",n6,n5,n2," ou: ",a)
