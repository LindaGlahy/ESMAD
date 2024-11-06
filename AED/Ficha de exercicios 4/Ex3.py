def positiveList(listNumber):
    '''
    Recebe diversas pontuações e devolve uma lista com as notas consideradas positivas, maiores que 10.
    '''
    newList = []
    for i in range(len(listNumber)):
        if listNumber[i] >= 10:
            newList.append(listNumber[i])
    return newList


listNumber = []
i=0
while i <10:
    try:
        number = int(input("Insira o {:n}º número: " .format(i+1)))
        if number < 0 or number > 20:
            raise ValueError()
    except ValueError:
        print("A pontuação deve ser entre [0-20]")
    except:
        print("Insira um valor válido")
    else:
        listNumber.append(number)
        i+=1

print("Pontuações positivas: ", positiveList(listNumber))