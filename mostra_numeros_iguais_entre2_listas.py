conjA = 0
n1 = int(input())
A = input().split(" ")
for x in A:
    conjA = conjA+1




conjB = 0
n2 = int(input())
B = input().split(" ")
for x in B:
    conjB = conjB+1




if conjB > conjA:
    print("0")   
else: 
    A = set(A).intersection(B)
    B = set(B).intersection(B)
    if A == B:
        print("1")
    else:
        print("0")

print(A,"    ",B)
print(len(B))        

