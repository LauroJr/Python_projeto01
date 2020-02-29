'''Se o salário for menor ou igual a 1751.81 terá um determinado desconto,
    e assim por diante.
'''


s = float(input())
if s <= 1751.81:
    inss = (s*8)/100
    print("Desconto do INSS: R$ {:.2f}".format(inss))
else:
    if s >= 1751.82 and s <= 2919.72:
        inss = (s*8)/100
        print("Desconto do INSS: R$ {:.2f}".format(inss))
    else:
        if s >= 2919.73 and s <= 5839.45:
            inss = (s*11)/100
            print("Desconto do INSS: R$ {:.2f}".format(inss))
        else:
            if s > 5839.45:
                s = 5839.45
                inss = (s*11)/100
                print("Desconto do INSS: R$ {:.2f}".format(inss))
                    
