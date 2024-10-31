numero = int(input("Digite um número entre 1 e 99: "))

if 1 <= numero <= 99:
    binario = ''
    
    while numero > 0:
        resto = numero % 2  
        binario = str(resto) + binario 
        numero //= 2  
    
    resultado = ' '.join(binario)
    
    print(f"Resultado: {resultado}")
else:
    print("Por favor, digite um número válido entre 1 e 99.")