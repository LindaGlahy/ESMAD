numero = int(input('Indique um número para fatoração: '))

if numero < 0:
    print('Precisa ser negativo')

elif numero == 0:
    print('Fatorial igual a 0')

for i in range(1, numero):
    numero *= i

print ("O fatorial é ", numero)