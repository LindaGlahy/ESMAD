num = int(input('Nº de termo a imprimir: '))
ultimo = 1
penultimo = 0

termos = "0, "
if num <= 1:
    termos = "0, "
if num == 2:
    termos = "0, 1, "
else:
    for i in range(1,num):
        novo = ultimo + penultimo
        termos +=  str(novo) + ", "
        ultimo = penultimo
        penultimo = novo

print(f"Primeiros {num} termos da sequencia de Fibonacci: {termos[:-2]}")