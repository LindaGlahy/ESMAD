def aboveAverage(listNumber):
    media = sum(listNumber)/len(listNumber)
    cont=0

    for numero in listNumber:
        if numero > media:
            cont+=1
    return cont


listNumber = []
for i in range(10):
    numero = int(input("Insira o {:n} número: " .format(i+1)))
    listNumber.append(numero)

print ('Existem {:n} números acima da média'.format(aboveAverage(listNumber)))