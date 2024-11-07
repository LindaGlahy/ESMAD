meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

listPluvio = []
leitura = 0
for i in range(12):
    leitura = int(input("Indique a faturação do mês de {:s}: " .format(meses[i])))
    novaLeitura = leitura
    if novaLeitura > leitura:
        listPluvio = (novaLeitura) + listPluvio
    elif novaLeitura <= leitura:
        listPluvio.append(novaLeitura)

print (listPluvio)