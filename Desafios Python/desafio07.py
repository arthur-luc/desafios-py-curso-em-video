#media aritmetica

#usei um sistema de repeticao para automatizar esse sistema
valorbool = True
while valorbool:
  n1 = int(input('Qual foi sua primeira nota?\n'))

  if n1 <0 or n1 >10:
    print('O valor precisa estar entre 0 e 10, repita o processo')
    continue
    
  n2 = int(input('Qual foi sua segunda nota?\n'))

  if n2 <0 or n2 >10:
    print('O valor precisa estar entre 0 e 10, repita o processo')
    continue

  else:
    print('Essa é a sua média {}'.format((n1+n2)/2))

  repetir = input('\nQuer repetir o processo?\nResponda com sim ou não:\n')

  if repetir == 'sim' or repetir == 'Sim':
    continue

  else:
    print('\nObrigado por usar o programa!')
    break