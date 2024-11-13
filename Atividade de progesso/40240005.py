cidades = ['Porto', 'Maia', 'Matosinhos', 'Vila do Conde', 'Póvoa de Varzim', 'Gondomar', 'Gaia'] # Nomes da cidade;

def dadosEstatistica(temp):
    '''
    Deve organizar os dados, realizar a média, localizar a temperatura mais distante da média
    e devolver a cidade correspondente da tal temperatura.
    '''
    media = sum(temp) / len(temp)                                                           # Calcula a media das temperaturas inseridas;


tempList = []
try:
    for i in range(7):                                                                      # Corre pela lista "cidades", item por item;
        temp = float(input("Indique a temperatura da cidade {:s}: (0-40) " .format(cidades[i])))   # Pede para introzir a temperatura de cada cidade;
        if temp < 0 or temp > 40:
            ValueError
        else:
            tempList.append(temp)
except ValueError:
    print("Indique um valor entre 0ºC e 40ºC")
except:
    print("Indique um valor válido")

print (tempList)