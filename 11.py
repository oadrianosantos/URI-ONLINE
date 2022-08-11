import math
a = input().split(" ")

A = float(a[0])
B = float(a[1])
C = float(a[2])

delta = (B**2)-(4*A*C)

if delta < 0 or A ==0:
    print("Impossivel calcular")
else:
    x1 = ((-1 * B) + math.sqrt(delta)) / (2 * A)
    x2 = ((-1 * B) - math.sqrt(delta)) / (2 * A)
    print("%s %1.5f" % ("R1 =", x1))
    print("%s %1.5f" % ("R2 =", x2))


