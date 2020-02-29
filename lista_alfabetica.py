# Digite dois numeros inteiros seguidos por espaços. O programa ira mostrar
# na sequência alfabética de acordo com o segundo numero digitado

n1, n2 = input().split(' ')
n1 = int(n1)
n2 = int(n2)
Lista_Nom = [0]*n1
pos = 0

for x in Lista_Nom:
    Lista_Nom[pos] = input()
    pos = pos+1
Lista_Nom.sort()
print(Lista_Nom[n2-1])
