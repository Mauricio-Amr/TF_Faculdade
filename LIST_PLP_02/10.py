''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    Data: 09/10/2021
    Lista: 02 - 10
    Enunciado: 10 – Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
    porcentagem do aumento. Exiba o valor do aumento e do novo salário.
    ----------------------------------------------------------------- '''

salario = float(input("Digite o salario : "))
aumento = float(input("Qual o aumento do salario : "))

salarioComAumento = salario+(salario * (aumento*0.01))

print(f'\nSeu salario de {salario}, teve um aumento de {aumento}%, o salario atual é de : {salarioComAumento} ')

