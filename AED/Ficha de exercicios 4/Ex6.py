def searchNumber(listNumber,search):
    '''
    '''

    pos = listNumber.index(search)

    return (pos)

listNumber = []
i=0
for i in range(10):
    number = int(input("Insira o {:n}º número: " .format(i+1)))
    listNumber.append(number)

search = input("Insira o número de procura: ")

print("O número {:.f} está na {:.f}ª posição" .format(search, searchNumber(listNumber,search)))
