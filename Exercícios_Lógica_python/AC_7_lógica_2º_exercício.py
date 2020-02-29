si = 0
m = 0
i = 1
while i != 0:
    i = int(input("Digite sua idade: "))
    si = si+i
    if i > 0:
        m = m+1        
if si > 0:
    mi = si/m
    print("A média das idades somadas é: ",mi,". A soma é: ",si," anos")
else:
    print("Não é possível resumir a conta pois não há entradas coerentes")
    
