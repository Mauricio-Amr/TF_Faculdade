''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 10/10/2021
    Lista: 04 - 13
    Enunciado: 13 – Escreva um programa que pergunte o valor inicial de uma divida e o juros mensal. Pergunte também o
    valor mensal que será pago. Imprima o número de meses para que a divida seja paga, o total pago e o total
    de juros pago.
    ----------------------------------------------------------------- '''


# quanto tempo para paga a divida, inicializar contador
meses = 0
#valorJuros = 0


valorDivida = float(input("Digite o valor da divida : "))
valorMensal = float(input("Digite o valor mensal para quitar a divida : "))
jurosMensal = float(input("Digite o Juros : "))

print(f'{valorMensal} = {jurosMensal:.2f} =  {valorDivida:.2f}')

# Juros mensal
if valorMensal > valorDivida*(jurosMensal/100):
    while valorDivida >= 0:

        valorJuros = valorDivida * (jurosMensal / 100)
        valorDivida = (valorDivida - valorMensal) + valorJuros
        meses += 1
        print(f'{meses} = {valorJuros:.2f} =  {valorDivida:.2f}')

        if valorDivida < valorMensal:
            meses += 1
            valorJuros = 0
            valorMensal = valorDivida
            valorDivida = valorDivida - valorMensal
            print(f'{meses} = {valorJuros:.2f} =  {valorDivida:.2f}')
            break


else:
    print(f'Proposta não atende')


# total pago

#juros não pode ser maior que o valor mensal

