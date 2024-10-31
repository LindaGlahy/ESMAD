def positiveList(listNumber):
    for i in range(len(listNumber)):
        if listNumber[i] >= 10:
            newList += i



listNumber = []
i = 0
while i < 10:
    try:
        number = int(input("Insira o {:n} número: " .format(i+1)))
        if number >= 10 and number <= 21:
            raise ValueError()
    except ValueError:
        print("A pontuação deve ser entre [0-20]")
    except:
        print("Insira um valor válido")
    else:
        listNumber.append(number)

newList = positiveList(listNumber)
print("Pontuações positivas: ", newList)