maior = 0
soma = 0
i = 0

while i < 10:
    numero = int(input("indique o {:n} numero:" .format(i+1)))
    if numero > 20:
        continue
    soma += numero
    i += 1
    if numero > maior:
        maior = numero

print ("A media e {:n}" .format(soma/10))
print ("O maior numero e {:n}" .format(maior))