list = []

while True:
    line = int(input("Insira o número de linhas deseja criar: "))
    column = int(input("Insira o número de colunas deseja criar: "))

    for i in range(line):
        list.append([])                         # Acrescenta uma lista vazia para cada linha
        for j in range(column):
            numero = int(input("Número: "))
            list[i].append(numero)              # Acrescenta à lista o numero lido

    for line in list:
        print(line)
    
    end = 0

    loop = input("Desejar fazer nova ordenação? (S/N): ")
    if loop.upper() == "N":
        break
    elif loop.upper() == "S":
        end+=1
    else:
        print("Insira uma resposta válida")

    if end > 0:
        False
        list = []