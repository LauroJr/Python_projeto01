''' Este programa Faz 5 Exercícios. Mostra qual maior n, se é par ou
    impar. E etc...
'''

print("===================")
a = int(input())
b = int(input())
if a > b:
    print(a)
if b > a:
    print(b)
if a == b:
    print(a)
print("===================")
a = int(input())
b = int(input())
if a > b:
    print("A eh maior")
if b > a:
    print("B eh maior")
if a == b:
    print("Iguais")
print("===================")
i = int(input())
if i < 16:
    print("nao eleitor")
if (i >= 18) and (i <= 65):
    print("eleitor obrigatorio")
if ((i >= 16) and (i <18)) or (i > 65):
    print("eleitor facultativo")
print("===================")
n = int(input())
if n%2 == 0:
    print("O numero eh",n,"e ele eh par")
else:
    print("O numero eh",n,"e ele eh impar")
print("==================")
l = float(input())
c = float(input())
a = float(input())
if ((l <=45) and (c<=56) and (a <=25)):
    print("PERMITIDA")
else:
    print("PROIBIDA")
