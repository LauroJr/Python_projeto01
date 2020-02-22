import math
print("AC 2 exercicio c")
a = float(input())
b = float(input())
c = float(input())
d = float(input())
R1 = ((a**2) + (3*b))
R1 =  (R1/c) + d
R2 = (((math.log10(a)) + math.e**(-b/c)) - (d**2/math.pi))
a1 = a**2
R3 = (a1**(1/3) * b**(1/3) + (c*d)) / (a+b+c+d)
R4 = ((a+b) * (c+d)) / (a*b*c*d)
R5 = (((a**2 + b**2) / (c*d)) - ((c**2 + d**2) / (a*b)))
Q = a+b+c+d
Q = Q**2
Qa = a**2
Qb = b**2
Qc = c**2 
Qd = d**2
Sq = Qa+Qb+Qc+Qd
Rc = a*b*c*d
Rc = Rc**(1/3)
print("i)",round(R1, 4))
print("ii)",round(R2, 4))
print("iii)",round(R3, 4))
print("iv)",round(R4, 4))
print("v)",round(R5, 4))
print("vi)",round(Q, 4))
print("vii)",round(Sq, 4))
print("viii)",round(Rc, 4))



