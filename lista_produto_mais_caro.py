# Adicione quantos produtos quiser a uma determinada lista. Depois print o mais caro
# e qual seu código.

a = 1
lista = []
aux = 0
cod = 0
qnt = 0
custo = 0
while a != 0:
    a, b, c = input().split(" ")
    a = int(a)
    b = int(b)
    c = float(c)
    total = b*c
    if total > aux:
        cod = a
        qnt = b
        custo = c
        t = total
        aux = total

if cod == 0 and qnt == 0 and custo == 0:
    print("nao tem compras")
else:
    print("Item mais caro")
    print("Codigo:",cod)
    print("Quantidade:",qnt)
    print("Custo: {:.2f}".format(t))



