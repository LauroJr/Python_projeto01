# digite uma sequência de número separados por espaço, onde serão incluso em uma lista
# de forma crescente

lista = input().split(" ")
pos = 0

for x in lista:
    lista[pos] = int(lista[pos])
    pos = pos+1
lista.sort()


m ='a'

while m != 'final':
    pos = 0
    msg = input().split(" ")
    if len(msg) == 2:
        m = msg[0]
        x = int(msg[1])
        if m == 'inserir':
            lista.append(x)
        else:
            lista.remove(x)
    else:
        m = msg[0]
        if m == 'parcial':
            lista.sort()                
            for x in lista:
                lista[pos] = str(lista[pos])
                pos = pos+1
            b = " ".join(lista)    
            print(b)
            pos = 0
            for x in lista:
                lista[pos] = int(lista[pos])
                pos=pos+1
        else:
            m = 'final'
            lista.sort()
            for x in lista:
                lista[pos] = str(lista[pos])
                pos = pos+1
            b = " ".join(lista)    
            print(b)
            pos = 0
            for x in lista:
                lista[pos] = int(lista[pos])
                pos=pos+1
