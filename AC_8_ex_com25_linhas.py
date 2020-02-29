conjA = 0
n1 = int(input())
lista1 = input().split(" ")
for x in lista1:
    conjA = conjA+1


conjB = 0
n2 = int(input())
lista2 = input().split(" ")
for x in lista2:
    conjB = conjB+1


if conjB > conjA:
    print("0")
else:
    cont = 0
    lista2 = set(lista1).intersection(lista2)
    lista1 = set(lista2).intersection(lista1)
    if lista1 == lista2:
        print("1")
    else:
        print("0")
