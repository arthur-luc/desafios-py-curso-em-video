#pintando paredes

largura = input('Qual a largura em metros da parede que você quer pintar?\n')
altura = input('E qual a altura?\n')
area = int(largura)*int(altura)

print('Você precisará de {} litros de tinta para pintar essa parede'.format(area/2))