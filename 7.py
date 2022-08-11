v = int(input())
global resto, a_100, b_50, c_20, d_10,e_5,f_2


if v >=100:
    a_100 = v//100
    resto = v%100
else:
    resto = v % 100
    a_100 = 0
if resto>=50:
    b_50 = resto // 50
    resto = resto % 50
else:
    resto = resto % 50
    b_50 =0
if resto >=20:
    c_20 = resto//20
    resto = resto%20
else:
    resto = resto % 20
    c_20 =0
if resto>=10:
    d_10 = resto//10
    resto = resto%10
else:
    resto = resto%10
    d_10 = 0
if resto>= 5:
    e_5 = resto//5
    resto = resto%5
else:
    resto = resto % 5
    e_5 =0
if resto>=2:
    f_2 = resto//2
    resto = resto%2
else:
    resto = resto%2
    f_2 = 0

g_1 = resto//1


print (v, "\n",
       a_100, "nota(s) de R$ 100,00", "\n",
       b_50, "nota(s) de R$ 50,00", "\n",
       c_20, "nota(s) de R$ 20,00", "\n",
       d_10, "nota(s) de R$ 10,00", "\n",
       e_5, "nota(s) de R$ 5,00", "\n",
       f_2, "nota(s) de R$ 2,00", "\n",
       g_1, "nota(s) de R$ 1,00", "\n"
)






