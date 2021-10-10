''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 10/10/2021
    Lista: 03 - 09
    Enunciado: 09 – Escreva um programa para aprovar o empréstimo bancário
    para compra de uma casa. O programa deve perguntar o valor da casa a
    comprar, o salário e a quantidade de anos a pagar. O valor da prestação
    mensal não pode ser superior a 30% do salário. Calcule o valor da
    prestação como sendo o valor da casa a comprar dividido pelo numero
    de meses a pagar.
    ----------------------------------------------------------------- '''


valorDoEmprestimo = float(input("Digite o valor do emprestimo : "))
valorDoSalario = float(input("Digite seu salario : "))
anosApagar = int(input("Digite as prestações : "))

prestacao = valorDoEmprestimo / (anosApagar)


if prestacao > valorDoSalario*0.3 :
    print("Emprestimo negado")
else:
    print('\n')
    print('#'*50)
    print(f"Valor do emprestimo  ................... {valorDoEmprestimo: .2f} ")
    print(f'Prestação  ............................. {prestacao:.2f}')
    print(f'Parcelas  ............................. {anosApagar}')
    print('#'*50)




