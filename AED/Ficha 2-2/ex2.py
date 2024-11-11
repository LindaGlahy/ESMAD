n1 = int(input("Indique o limite inferior: "))
n2 = int(input("Indique o limite superior: "))

soma = 0

for i in range(n1,n2+1):
    if i % 2 == 0:
        soma += i

print(f"A soma de todos os pares entre {n1} e {n2} é", soma)