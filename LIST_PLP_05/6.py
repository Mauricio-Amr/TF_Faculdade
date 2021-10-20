''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 10/10/2021
    Lista: 05 - 06
    Enunciado: 06 – Modifique o programa da questão 05 para trabalhar
    com duas filas. Para facilitar seu trabalho, considere o comando A
    para atendimento da fila 1; e B, para atendimento da fila 2. O mesmo
    para chegada de clientes:
    F para fila 1; e G, para fila 2.
    ----------------------------------------------------------------- '''

fila_1 = []
fila_2 = []

contador_A = 1
contador_B = 1

while True:
    entrada = input('A - Senha fila comum \n'
                    'B - Senha fila preferencial\n'
                    'F - Atender fila comum\n'
                    'G - Atender fila preferencial\n'
                    'S - Sair\n'
                    '\nDigite sua a Entrada : ').upper()

    # Chegada de cliente A

    if entrada == 'A':

        fila_1.append(contador_A)
        contador_A += 1

    # Chegada de cliente B
    elif entrada == 'B':
        fila_2.append(contador_B)
        contador_B += 1

    # Atende fila A
    elif entrada == 'F':
        # verificar se fila B esta com cliente
        if len(fila_2) >= 5:
            print('\nTEMOS CLIENTE NA FILA PREFERENCIAL'
                  '\n\n ATENDA A FILA PREFERENCIAL')

        else:
            fila_1.remove(fila_1[0])

    # Atende fila B
    elif entrada == 'G':
        fila_2.remove(fila_2[0])

    # Sair
    elif entrada == 'S':
        print('\n FINALIZANDO SISTEMA'
              '\n\nMUITO OBRIGADO')
        break

    print(f'\nFILA COMUM :        {fila_1}'
          f'\nFILA PREFERENCIAL : {fila_2}\n')
