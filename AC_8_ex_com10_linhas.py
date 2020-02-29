n1 = int(input())
A = input().split(" ")
n2 = int(input())
B = input().split(" ")    
A = set(A).intersection(B)
B = set(B).intersection(B)


if A == B:
    print("1")
else:
    print("0")
    
#print(A,"    ",B)
#print(len(B))
