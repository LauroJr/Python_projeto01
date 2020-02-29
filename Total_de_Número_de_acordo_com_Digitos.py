pos = 0
quantidade = 0
msg,dig = input().split(" ")
for x in msg:
    if msg[pos] == dig:
        quantidade = quantidade+1
    pos = pos+1    
print(quantidade)



