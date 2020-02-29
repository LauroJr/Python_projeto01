# Exiba tabuadas de 1 á 9 no intervalo escolhido por ti. EX: Se você digitar 6 e 8,
# aparecerão tabuadas do 6, 7 e 8. Se as entradas forem 2 e 7, aparecderão tabuadas
# do 2, 3, 4, 5, 6 e 7.


n1 = 0
n2 = 10
while n1 < 1 or n1 > 9:
    n1 = int(input())
    if n1 < 1 or n1 > 9:
        print("Insira um número inicial entre 1 e 9")
while n2 < 1 or n2 > 9:        
    n2 = int(input())    
    if n2 < 1 or n2 > 9:
        print("Insira um número final entre 1 e 9")
    if n1 > n2:
        print("Nenhuma tabuada nesse intervalo")
    else:
        if n1 > 0 and n2 < 10 and n1 < n2 or n1 == n2:
            tab1 = n1
            tab2 = n2
            c = 1
            while c <= 9:
                r = tab1*c
                print(tab1,"x",c,"=",r)
                c = c+1
                if c > 9 and tab1 < tab2:
                    print("")
                    c = c-9
                    tab1 = tab1 + 1
                    while c <= 9:
                        r = tab1*c
                        print(tab1,"x",c,"=",r)
                        c = c+1
                        if c > 9 and tab1 < tab2:
                            print("")
                            c = c-9
                            tab1 = tab1 + 1
                            while c <= 9:
                                r = tab1*c
                                print(tab1,"x",c,"=",r)
                                c = c+1
                                if c > 9 and tab1 < tab2:
                                    print("")
                                    c = c-9
                                    tab1 = tab1 + 1
                                    while c <= 9:
                                        r = tab1*c
                                        print(tab1,"x",c,"=",r)
                                        c = c+1
                                        if c > 9 and tab1 < tab2:
                                            print()
                                            c = c-9
                                            tab1 = tab1 + 1
                                            while c <= 9:
                                                r = tab1*c
                                                print(tab1,"x",c,"=",r)
                                                c = c+1
                                                if c > 9 and tab1 < tab2:
                                                    print("")
                                                    c = c-9
                                                    tab1 = tab1 + 1
                                                    while c <= 9:
                                                        r = tab1*c
                                                        print(tab1,"x",c,"=",r)
                                                        c = c+1
                                                        if c > 9 and tab1 < tab2:
                                                            print("")
                                                            c = c-9
                                                            tab1 = tab1 + 1
                                                            while c <= 9:
                                                                r = tab1*c
                                                                print(tab1,"x",c,"=",r)
                                                                c = c+1
                                                                if c > 9 and tab1 < tab2:
                                                                    print("")
                                                                    c = c-9
                                                                    tab1 = tab1 + 1
                                                                    while c <= 9:
                                                                        r = tab1*c
                                                                        print(tab1,"x",c,"=",r)
                                                                        c = c+1
                                                                        if c > 9 and tab1 < tab2:
                                                                            print("")
                                                                            c = c-9
                                                                            tab1 = tab1 + 1
                                                                            while c <= 9:
                                                                                r = tab1*c
                                                                                print(tab1,"x",c,"=",r)
                                                                                c = c+1                             
