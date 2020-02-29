# Insira, remova itens de uma lista

entrada = 't'
pos = 0
Lista_p = []
while entrada != 's':
    Lista_pedido = input().split()
    if Lista_pedido[0] == 'a':
        entrada = 'a' 
        aux = Lista_pedido[1]
        Lista_p.append(aux)
    else:
        if Lista_pedido[0] == 'r':
            entrada = 'r'
            aux = Lista_pedido[1]
            if aux in Lista_p:
                print("removido")
                Lista_p.remove(aux)
            else:
                print("falha")
        else:
            if Lista_pedido[0] == 'p' and len(Lista_p) >= 1:
                entrada = 'p'
                b = " ".join(Lista_p)
                print(b)
            else:
                if Lista_pedido[0] == 'p': 
                    print("vazia")
                else:
                    entrada = 's'
