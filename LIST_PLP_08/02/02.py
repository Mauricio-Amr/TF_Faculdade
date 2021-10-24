""" -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 10/10/2021
    Lista: 08 - 02
    Enunciado: 02 – Crie um programa que leia os arquivos pares.txt
    e impares.txt (gerado na questão 01) e que crie um
    só arquivo paresimpares.txt com todas as linhas dos outros
    dois arquivos, de forma a preservar a ordem
    numérica.

    ----------------------------------------------------------------- """

with open("pares.txt", "r") as arqPares:
    with open("impares.txt", "r") as arqImpares:
        with open("paresimpares.txt", "w") as paresimpares:

            listaNumero = []
            for impar in arqImpares.readlines():
                impar = impar.replace("\n", "")
                listaNumero.append(impar)
            for par in arqPares.readlines():
                par = par.replace("\n", "")
                listaNumero.append(par)

            listaNumero.sort(key=int)
            print(listaNumero)
            for num in listaNumero:
                paresimpares.write(f'{num}\n')

arqPares.close()
arqImpares.close()
paresimpares.close()
