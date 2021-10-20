''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 10/10/2021
    Lista: 04 - 16
    Enunciado:16 – Escreva um programa que leia um valor e que
    imprima a quantidade de cédulas necessárias para pagar esse
    mesmo valor. Para simplificar utilize números inteiros e com
    cédulas de R$50, R$20, R$10, R$4 e R$1.
    Após concluído, testes com os seguintes valores: 50, 745, 384, 2, 7 e 1.
    ----------------------------------------------------------------- '''
import math
try:
    valor = int( input('Digite o valor a ser sacado : '))

    nota_50 = 0
    nota_20 = 0
    nota_10 = 0
    nota_4 = 0
    nota_1 = 0

    while valor > 0:
        if valor >= 50:
            nota_50 = math.floor(valor / 50)
            valor = valor % 50
            print(f'Retirado nota(s) de 50 : {nota_50} ')

        elif valor >= 20:
            nota_20 = math.floor(valor / 20)
            valor = valor % 20
            print(f'Retirado nota(s) de 20 : {nota_20} ')

        elif valor >= 10:
            nota_10 = math.floor(valor / 10)
            valor = valor % 10
            print(f'Retirado nota(s) de 10 : {nota_10} ')

        elif valor >= 4:
            nota_4 = math.floor(valor / 4)
            valor = valor % 4
            print(f'Retirado nota(s) de 4 : {nota_4} ')

        elif valor >= 1:
            nota_1 = math.floor(valor / 1)
            valor = valor % 1
            print(f'Retirado nota(s) de 1 : {nota_1} ')

        else :
            print('finalizar')

except :
    print(f'Valor digitado não é valido')