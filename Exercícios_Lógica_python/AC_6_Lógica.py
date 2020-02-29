p40 = 0
sh = 0
s50 = 0
c = 1
m = 0
while c <= 5:
    print("========================")
    print("CADASTRO DA ",c,"º PESSOA:")
    i = int(input("Digite sua idade: "))
    p = int(input("Digite seu peso: "))
    h = float(input("Digite sua altura: "))
    h = round(h, 2)
    if i > 50:
        s50 = s50+1
    if i >=10 and i <=20:
        m = m + 1 
        sh = sh+h
        sh = round(sh, 2)
    if p < 40:
        p40 = p40 + 1
    c = c + 1
    if m > 0:
        m1 = sh/m
        m1 = round(m1, 2) 
p1 = (p40/5)*100
print("============================================================")
print(s50," Pessoa(s) com idade superior a 50 anos.")
if m > 0:
    print("A média das alturas das pessoas entre 10 e 20 anos é: {:.2f}".format(m1))
else:
        print("Não existe pessoas entre 10 e 20 anos")
print(p1,"% das pessoas com peso inferior á 40 Kg")
