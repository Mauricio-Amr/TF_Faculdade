''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 10/10/2021
    Lista: 05 - 15
    Enunciado: 15 – A lista de temperatura de Mons, na Belgica, foi
    armazenada na lista T = [-10, -8, 0, 1, 2, 5, -2, -4].
    Faça um programa que imprima a menor e a maior temperatura,
    assim como a temperatura média.
    ----------------------------------------------------------------- '''

T = [-10, -8, 0, 1, 2, 5, -2, -4]

print(f'Lista de temperaturas \n'
      f'Temp : {T}\n\n')

media = sum(temp for temp in T)/len(T)
T.sort()

print(
      f'Menor Temperatura  : {T[0]}\n'
      f'Maior Temperatura  : {T[-1]}\n'
      f'Media Temperatura  : {media}\n'
      )
