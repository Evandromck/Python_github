from datetime import date 
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa neasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else: 
        totmenor += 1

print('Ao tod ')

