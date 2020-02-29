lista = input().split(" ")
pos = 0

m ='a'

while m != 'final':
    msg = input().split(" ")
    if len(msg) == 2:
        m = msg[0]
        x = msg[1]
        if m == 'inserir':
            lista.append(x)
            lista.sort()
        else:
            lista.remove(x)
            lista.sort()
    else:
        m = msg[0]
        if m == 'parcial':
            lista.sort()
            b = " ".join(lista)
            print(b)
        else:
            m = 'final'
            lista.sort()
            b = " ".join(lista)
            print(b)
