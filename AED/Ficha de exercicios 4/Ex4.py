def positiveList(listNumber, listName):
    '''
    Recebe diversos nomes e suas respectivas pontuações e devolve uma lista com os nomes e as pontuações consideradas positivas, maiores que 10.
    '''
    newListNumber = []
    newListName = []
    for i in range(0, len(listNumber)):
        if listNumber[i] >= 10:
            newListNumber.append(listNumber[i])
            newListName.append(listName[i])
    return newListNumber, newListName


listNumber = []
listName = []

i=0
while i <10:
    try:
        name = (input("Insira a nome do {:n}º participante: " .format(i+1)))        
        number = int(input("Insira a pontuação: " .format(i+1)))
        if number < 0 or number > 20:
            raise ValueError()
    except ValueError:
        print("A pontuação deve ser entre [0-20]")
    except:
        print("Insira um valor válido")
    else:
        listName.append(name)
        listNumber.append(number)
        i+=1

newListNumber, newListName = positiveList(listNumber, listName)
if len(newListNumber) == 0:
    print ("Não há pontuações positivas")
else:
    print ("\n\nPontuações positivas:" , "\n", newListName, "\n", (newListNumber))