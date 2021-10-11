''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 10/10/2021
    Lista: 04 - 14
    Enunciado:14 – Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que
    o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma
    e a média aritmética.
    ----------------------------------------------------------------- '''

numerosInteiros = []


while True:
    digito  = int (input('Digite um numero inteiro'))
    numerosInteiros.append(digito)

    if digito == 0:
        tamLista = len(numerosInteiros)
        soma =sum([x for x in numerosInteiros])
        media = soma/tamLista

        print(f'total de digitos : {tamLista}\n'
              f'soma dos digitos : {soma}\n'
              f'media : {media}\n'
              )
        break
