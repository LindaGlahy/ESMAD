meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def maiorFaturacao(listFaturacao):
    '''
    '''

    maior = max(listFaturacao)         # Maior valor
    pos = listFaturacao.index(maior)   # posição do maior valor na lista

    return (meses[pos])

def menorFaturacao(listFaturacao):
    '''
    '''

    menor = min(listFaturacao)         # Menor valor
    pos = listFaturacao.index(menor)   # posição do menor valor na lista

    return (meses[pos])

def mediaFaturacao(listFaturacao):
    '''
    '''

    media = sum(listFaturacao) / len(listFaturacao)

    return media

listFaturacao = []
for i in range(12):
    faturacao = int(input("Indique a faturação do mês de {:s}: " .format(meses[i])))
    listFaturacao.append(faturacao)


print ("Mês de maior faturação: ", (maiorFaturacao(listFaturacao)))
print ("Mês de menor faturação: ", (menorFaturacao(listFaturacao)))
print ("Média da faturação: ", (mediaFaturacao(listFaturacao)))