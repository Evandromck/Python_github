#15 fiz sozinho aluguel de um carro com o km
km = float(input('Qual a km do carro ?'))
qntdia = int(input('Qual a quantidade de dias ?'))
custdia = qntdia * 60
rodado = 0.15 * km
total = custdia + rodado
print('O valor total do alugue >> {}'.format(total))