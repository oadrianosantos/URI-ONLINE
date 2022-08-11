a = input().split(" ")

A = int(a[0])
B = int(a[1])
C = int(a[2])

MAIOR = int(((A+B+abs(A-B))/2))
MAIOR = int(((MAIOR+B+abs(MAIOR-B))/2))
MAIOR = int(((MAIOR+C+abs(MAIOR-C))/2))

print(MAIOR, "eh o maior")

