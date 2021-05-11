import math
an = float(input('Digite o ângulo que voce deseja: '))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO {:.2f}'.format(an, seno))
seno = math.cos(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, seno))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem a TAGENTE de {:.2f}'.format(an, tangente))