''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 09/10/2021
    Lista: 01 - 06
    Enunciado: 06 – Escreva o programa que receba o valor
    do salário, do aumento (%) e calcule o valor do novo salário.
    Considere o salário de R$ 750,00 e o aumento de 15%.
    ----------------------------------------------------------------- '''


salario = float(input("Digite o salario : "))
aumento = float(input("Qual o aumento do salario : "))

salarioComAumento = salario+(salario * (aumento*0.01))

print(f'\nSeu salario de {salario},'
      f' teve um aumento de {aumento}%,'
      f' o salario atual é de : {salarioComAumento} ')

