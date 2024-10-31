def  heartRate(fc):
    if fc < 80:
        return('treino aeróbico')
    if fc < 100:
        return('treino cardiovascular')
    if fc < 120:
        return('treino aeróbico ideal')
    if fc < 140:
        return('treino anaeróbico')

fc = int(input("Indique sua frequência cardiaca: "))
print (heartRate(fc))