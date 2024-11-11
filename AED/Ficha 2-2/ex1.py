numero = int(input("Indique um número:"))


if numero < 0:
    print ("Indique um valor positivo")
elif numero == 0:
    print ("Fatorial de 0 é 1")
elif numero > 0:
    for i in range(1,numero):
        numero *= i
    print (f"Fatorial é", numero)
else:
    print("Indique um valor válido!")