tempo = int(input("Indique o tempo em segundos: "))
horas = int(tempo / 3600)
minutos = int((tempo/ 60)-horas*60)
segundos = tempo % 60
print('')
print (f'{horas} horas, {minutos} minutos, {segundos} segundos')
