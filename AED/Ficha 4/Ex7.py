meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def pluviosidade(listPluvio):
    '''
    '''
    listPluvio.sort(reverse=True)
    for i in range(12):
        print(listPluvio[i])

def pluviosidade2(listPluvio):
    '''
    '''
    listPluvio2 = listPluvio.copy()
    listPluvio2.sort(reverse=True)
    print("\n")
    print("Meses \t Pluviosidade")
    for i in range(12):
        pos = listPluvio.index(listPluvio2[i])
        print(meses[pos], "\t", listPluvio2[i])

listPluvio = []
for i in range(12):
    leitura = int(input("Indique a faturação do mês de {:s}: " .format(meses[i])))
    listPluvio.append(leitura)

pluviosidade2(listPluvio)