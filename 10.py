N = input().split(" ")

A = int(N[0])
B = int(N[1])
C = int(N[2])
D = int(N[3])

if B > C:
    if D > A:

        if (C+D)>(A+B):
            if C >0:
                if D >0:
                    if A%2 ==0:

                        print("Valores aceitos")

else:
    print("Valores não aceitos")
