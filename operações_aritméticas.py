''' Este programa recebe um número N real positivo e não nulo, e faz as seguintes operações:
Eleva o n a potencia de 2 - Eleva o n a potencia de "e" - Raiz de n - raiz de n sobre 3 - raiz de n sobre n -
e * n - PI / n - log na base 7 n- log na base e n - log na base pi n
'''

import math
print("AC 2 PYTHON")
n = float(input())
v1 = n**2 # potência 
v2 = n**math.e # potência de "e"
v3 = math.sqrt(n) # raiz quadrada
v4 = n**(1/3) # raiz cubica
v5 = n**(1/n) # raiz de n, ou seja, do próprio valor
v6 = n*math.e # n vezes "e"
v7 = math.pi/n 
v8 = math.log(n, 7) # esta função descobre qual a potência. EX: para saber qual potência a base 7 é elevada para dar N, usamos este comando
v9 = math.log(n)
v10 = math.log(n, (math.pi)) # descobre qual potência que PI precisa ter para resultar em N
print("i) ",v1)
print("ii) ",v2)
print("iii) ",v3)
print("iv) ",v4)
print("v) ",v5)
print("vi) ",v6)
print("vii) ",v7)
print("viii) ",v8)
print("ix) ",v9)
print("x) ",v10)
