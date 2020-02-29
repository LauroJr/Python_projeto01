pos = 0
ano = input().split(' ')

for xxxx in ano:
    a = int(ano[pos])
    if a < 1000 or a > 9999:
        print("Ano invalido")
    else:
        if a % 4 == 0 or a % 400 == 0 and a % 100 !=0:
            if a > 2019:
                print("O ano",a,"serah bissexto")
            else:
                if a < 2019:
                    print("O ano",a,"foi bissexto")
        else:
            print("O ano",a,"NAO eh bissexto")
    pos = pos + 1






    
  
