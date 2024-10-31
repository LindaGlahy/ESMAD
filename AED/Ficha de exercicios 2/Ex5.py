numero = int(input('Número:'))
counter = 0

for i in range(2,numero+1):
    if numero % i == 0:
        counter += 1
if counter == 1:
    print (f'O número {numero} é primo')
else:
    print (f'O número {numero} não é primo')