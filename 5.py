r = input("DIGITE OS NÚMEROS")
V = r.split(" ")
A = float(V[0])
B = float(V[1])
C = float(V[2])

area_t = (A * C) / 2
area_c = (3.14159 * (C ** 2))
area_tra = ((A + B) * C) / 2
area_q = B ** 2
area_r = A * B

list_A = [area_t, area_c, area_tra, area_q, area_r]
list_B = ["TRIAGULO:", "CIRCULO:", "TRAPEZIO:", "QUADRADO:", "RETANGULO:" ]

for i in range(0, 5):
    print ("%s %1.3f"%(list_B[i], list_A[i]))
