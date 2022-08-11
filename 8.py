v = float(input())
list_n = []
if v>0 and v<1000000.00:
    list_n.append(int((v//100)))
    resto = v%100.00
    list_n.append(resto//50)
    resto = resto%50.00
    list_n.append(resto//20)
    resto = resto%20.00
    list_n.append(resto//10)
    resto = resto%10.00
    list_n.append(resto//5)
    resto = resto%5.00
    list_n.append(resto//2)
    resto = resto%2
    list_n.append(resto)

print("%1.2f"%(v))
print(list_n[0], "nota(s) de R$ 100,00")
print(list_n[1],"nota(s) de R$ 50,00")
print(list_n[2],"nota(s) de R$ 20,00")
print(list_n[3],"nota(s) de R$ 10,00")
print(list_n[4],"nota(s) de R$ 5,00")
print(list_n[5],"nota(s) de R$ 2,00")
print(list_n[6],"nota(s) de R$ 1,00")