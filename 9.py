s = int(input())

horas = s//3600
resto = s%3600
minutos =  resto//60
resto = resto%60
segundos = resto

f = str(horas)+":"+str(minutos)+":"+str(segundos)

print(f)

