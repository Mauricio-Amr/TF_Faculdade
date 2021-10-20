''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 09/10/2021
    Lista: 02 - 12
    Enunciado: 12 – Escreva um programa que calcule o tempo de
    uma viagem de carro. Pergunte a distância a percorrer
    e a velocidade média esperada para a viagem.
    ----------------------------------------------------------------- '''

distanciaPercorrer = float(input("Digite a distancia a percorrer em Km : "))
velocidadeMedia = float(input("Digite a velocidade Media em Km/h : "))

tempo = distanciaPercorrer / velocidadeMedia


print(f'O tempo para percorrer {distanciaPercorrer} é de {tempo} horas')


