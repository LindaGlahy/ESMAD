def searchNumber(listNumber,search):
    '''
    '''

    numberSearch = listNumber.index(search)
    return (numberSearch)

listNumber = []
i=0
try:
    for i in range(10):
        number = int(input("Insira o {:n}º número: " .format(i+1)))
        listNumber.append(number)
except:
    print ("Insira um valor válido!")

search = input("Insira o número de procura: ")

print("O número {search} está na {:n}ª posição" .format(searchNumber(listNumber,search)))
