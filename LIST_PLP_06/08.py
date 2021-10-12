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

while True:
    nome = input('Digite o nome do aluno ')
    nota_1 = input('Digite a primeira nota')
    nota_2 = input('Digite a segunda nota')

    notas = {nome : [nota_1 , nota_2]}