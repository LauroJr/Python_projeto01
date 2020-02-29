''' Este programa recebe 4 entrada, que por sua vez são as notas de um aluno, e
    pesos 2, 2, 3  - e caulcula se o aluno será reprovado ou não.
'''

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
m = (n1*2 + n2*2 + n3*3)/7
m = round(m, 1)
f = n4*100
if f < 75:
    print("Frequencia: {:.0f}%".format(f))
    print("Media:",m)
    print("Aluno reprovado por faltas!")
else:
    if m >= 9 and f >= 75:
        print("Frequencia: {:.0f}%".format(f))
        print("Media:",m)
        print("Aluno aprovado com louvor!")
    else:
        if m >= 6 and m < 9 and f >= 75:
            print("Frequencia: {:.0f}%".format(f))
            print("Media:",m) 
            print("Aluno aprovado!")
        else:
            if m >= 4 and m < 6 and f >= 75:
                print("Frequencia: {:.0f}%".format(f))
                print("Media:",m)
                print("Aluno de recuperação!")
            else:
                if m < 4 and f >= 75:
                    print("Frequencia: {:.0f}%".format(f))
                    print("Media:",m)
                    print("Aluno reprovado!")
        
        
    
