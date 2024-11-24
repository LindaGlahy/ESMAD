from unicodedata import normalize

source = 'Arapeí'
target = normalize('NFKD', source).encode('ASCII','ignore').decode('ASCII')
print(target)