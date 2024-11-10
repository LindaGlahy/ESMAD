n1 = int(input('Insira número limite inferior: '))
n2 = int(input('Insira número limite superior: '))
resul = 0

for i in range(n1,n2+1):
    if i % 2 == 0:
        resul += i
    
print (f'A soma de todos os números entre {n1} e {n2} é', resul)
