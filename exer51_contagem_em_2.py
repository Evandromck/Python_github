primeiro = int(input('primeiro termo'))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão #FORMULA DA RAZÃO DA CONTAGEM DE PULAR NUMEROS 
for c in range (primeiro, décimo, razão, razão):
    print('{}'.format(c), end='->')
print('ACABOU')    

