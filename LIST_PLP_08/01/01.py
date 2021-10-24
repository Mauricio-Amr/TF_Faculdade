''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 10/10/2021
    Lista: 08 - 01
    Enunciado: 01 – Crie 3 arquivos de nome numeros.txt, pares.txt
    e impares.txt do número 1 ao número 500. Cada lista
    deve conter os seguintes conjuntos numéricos:
    numeros.txt - todos os números de 1 a 500,
    pares.txt - todos os números pares de 1 a 500 e
    impares.txt - todos os números ímpares de 1 a 500.
    ----------------------------------------------------------------- '''
with open("numeros.txt", 'w') as numero:
    with open("pares.txt", 'w') as pares:
        with open("impares.txt", "w") as impares:

            for num in range(1,500):
                numero.write(f'{num}\n')
                if num % 2 == 0:
                    pares.write(f'{num}\n')
                else:
                    impares.write((f'{num}\n'))