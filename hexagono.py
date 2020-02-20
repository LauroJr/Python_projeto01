'''
Escreva um programa em Python3 que peça o valor do lado de um hexágono regular, 
calcule e imprima sua área e seu perímetro.
'''

import math
L=float(input())
r=math.sqrt(3)
a=((L**2*3)*r)/2
p=L*6
print("Lado do hexagono:",L,"metros,")
print("Area:",a,"metros quadrados,")
print("Perimetro:",p,"metros.")