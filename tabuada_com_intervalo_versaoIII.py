def TABUADA(x1, x2):
    while x1 < x2:
        c = 1
        while c <= 9:
            r = x1*c
            print(x1,"x",c,"=",r)
            c = c+1
            if c > 9 and x1 < x2:
                print("")
                c = c-9
                x1 = x1 + 1


def TABUADA_REPETIDA(t1, t2):
    c = 1
    while c <= 9:
        r = t1*c
        print(t1,"x",c,"=",r)
        c = c+1



n1 = int(input())
while n1 < 1 or n1 > 9:
        print("Insira um número inicial entre 1 e 9")
        n1 = int(input())
n2 = int(input())        
while n2 < 1 or n2 > 9:                
        print("Insira um número final entre 1 e 9")
        n2 = int(input())
if n1 > n2:
    print("Nenhuma tabuada nesse intervalo")
else:
    if n1 == n2:
        TABUADA_REPETIDA(n1, n2)
    else:
        TABUADA(n1, n2)

    
    
    
