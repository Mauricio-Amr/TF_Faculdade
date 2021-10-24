""" -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 10/10/2021
    Lista: 08 - 03
    Enunciado: 03 – Crie um programa que inverta a ordem das linhas
    do arquivo numeros.txt. A primeira linha deve conter o maior
    número; e a última, o menor.

    ----------------------------------------------------------------- """
with open("numeros.txt", "r") as numeros:
    ordenarNumero = []
    for num in numeros.readlines():
        ordenarNumero.append(num)

    ordenarNumero.sort(key=int, reverse=True)
with open("numeros.txt", 'w') as numeros:
    for num in ordenarNumero:
        numeros.write(num)

numeros.close()
