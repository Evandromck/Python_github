#11 ok
largura = float (input ('Qual a largura da parede'))
altura = float(input('Qual a altura da parede?'))
área = largura*altura
print('Sua parede tem {}x{} e sua aria e {}m2.'.format(largura, altura, área))
tinta = área / 2
print('para pintar essa parede voce precisará de {}l de tinta.'.format(tinta))