def maior(*numeros):
    maior_numero = numeros[0]
    for i in range(len(numeros)):
        if numeros[i] > maior_numero:
            maior_numero = numeros[i]
    
    return maior_numero
    
print (maior())