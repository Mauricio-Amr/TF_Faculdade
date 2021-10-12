''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 10/10/2021
    Lista: 06 - 08
    Enunciado: 08 – Escreva um programa que lê duas notas de vários
    alunos e armazena tais notas em um dicionário, onde a chave é o
    nome do aluno. A entrada de dados deve terminar quando for lida
    uma string vazia como nome.
    Escreva uma função que retorna a média do aluno, dado seu nome.
    ----------------------------------------------------------------- '''

def pesquisarAluno ( dicionario, procurar):
    for key, valor in dicionario.items():
        if procurar in key:
            notaM1 = int(valor[0])
            notaM2 = int(valor[1])
            media = notaM1 + notaM2 / 2
            print(f'Aluno  : {key} \n'
                  f'Nota 1 : {valor[0]}\n'
                  f'Nota 2 : {valor[1]}\n'
                  f'Media  : {media}\n\n')
        else:
            print('aluno não cadastrado\n')




notas = {}
sair = ' '
while True:
    opcao  = input("Digite uma das opções \n"
                   "1 - Cadastro de aluno / nota \n"
                   "2 - Media do aluno \n"
                   "S - Sair"
                   "Opção : ")


    if opcao == '1' :
        print ('\nCadastro e aluno /nota')
        nome = input('Digite o nome do aluno :  ')
        nota_1 = input('Digite a primeira nota 1 : ')
        nota_2 = input('Digite a segunda nota 2 : ')

        notas.update({nome: [nota_1, nota_2 ]})
        print(f'lista cadastrada\n {notas}')

        sair = input('\nDeseja sair , precione "S". ').lower()


    elif opcao == '2':
        procura = input('\nDigite o nome do aluno na lista : ' )
        pesquisarAluno(notas,procura)

    elif sair == 's' or opcao == 's':
        break


