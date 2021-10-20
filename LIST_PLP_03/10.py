''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 10/10/2021
    Lista: 03 - 10
    Enunciado: 10 – Escreva um programa que calcule o preço a
    pagar pelo fornecimento de energia elétrica. Pergunte a
    quantidade de kWh consumida e o tipo de instalação:
    R para residencial, I para industrial e C para comércios.
    Calcule o preço a pagar de acordo com a tabela a seguir:
    • Residencial: Até 500 kWh – R$ 0,40 e acima de 500 kWh – R$ 0,65.
    • Comercial: Até 1000 kWh – R$ 0,55 e acima de 1000 kWh – R$ 0,60.
    • Industrial: Até 5000 kWh – R$ 0,55 e acima de 5000 kWh – R$ 0,60.
    ----------------------------------------------------------------- '''


def resultado(tipoinstalacao, consumonormal, valorkWh,
              valorconsumonormal, consumoEx, valorkwhex=0, valorconsumoex=0, valorpagar=0):
    print('#' * 50)
    print(f'Tipo de instalação  .......................... {tipoinstalacao}')
    print(f'Consumo normal {consumonormal} * {valorkWh}  ...................R$ {valorconsumonormal:.2f}')
    print(f'Consumo excendete {consumoEx} * {valorkwhex} ..............R$ {valorconsumoex}')
    print(f'Valor total .................................R$ {valorpagar:.2f}')
    print('#' * 50)
    print('\n')


vlResidencia500 = 0.4
vlResidencia500ac = 0.65
vlComercio1000 = 0.55
vlComercio1000ac = 0.60
vlIndustrial5000 = 0.55
vlIndustrial5000ac = 0.60
valorPagarExc = 0
valorExcedente = 0

while True:
    print("R - Residencia\nI - Industrial\nC - Comercio\n")
    instalacao = input('Digite uma das opçoes acima : ').lower()
    qtDeWatts = float(input('Digite o  consumo em kWh : '))

    if instalacao == 'r':
        if qtDeWatts <= 500:
            if qtDeWatts < 500:
                consumoNormal = qtDeWatts
            else:
                consumoNormal = 500

            valorPagarTotalNormal = qtDeWatts * vlResidencia500
            valorPagarTotal = valorPagarTotalNormal

            resultado(instalacao,
                      consumoNormal,
                      vlResidencia500,
                      valorPagarTotalNormal,
                      valorExcedente,
                      vlResidencia500ac,
                      valorPagarExc,
                      valorPagarTotal
                      )


        else:
            if qtDeWatts < 500:
                consumoNormal = qtDeWatts
            else:
                consumoNormal = 500

            valorPagarTotalNormal = qtDeWatts * vlResidencia500
            valorExcedente = qtDeWatts - 500
            valorPagar500 = 500 * vlResidencia500
            valorPagarExc = valorExcedente * vlResidencia500ac
            valorPagarTotal = valorPagar500 + valorPagarExc

            resultado(instalacao,
                      consumoNormal,
                      vlResidencia500,
                      valorPagar500,
                      valorExcedente,
                      vlResidencia500ac,
                      valorPagarExc,
                      valorPagarTotal
                      )

    if instalacao == 'c':
        if qtDeWatts <= 1000:
            if qtDeWatts < 1000:
                consumoNormal = qtDeWatts
            else:
                consumoNormal = 1000

            valorPagarTotalNormal = qtDeWatts * vlComercio1000
            valorPagarTotal = valorPagarTotalNormal

            resultado(instalacao,
                      consumoNormal,
                      vlComercio1000,
                      valorPagarTotalNormal,
                      valorExcedente,
                      vlComercio1000ac,
                      valorPagarExc,
                      valorPagarTotal
                      )


        else:
            if qtDeWatts < 1000:
                consumoNormal = qtDeWatts
            else:
                consumoNormal = 1000

            valorPagarTotalNormal = qtDeWatts * vlComercio1000
            valorPagarTotal = valorPagarTotalNormal

            valorExcedente = qtDeWatts - 1000
            valorPagar1000 = 1000 * vlComercio1000
            valorPagarExc = valorExcedente * vlComercio1000ac
            valorPagarTotal = valorPagar1000 + valorPagarExc

            resultado(instalacao,
                      consumoNormal,
                      vlComercio1000,
                      valorPagar1000,
                      valorExcedente,
                      vlComercio1000ac,
                      valorPagarExc,
                      valorPagarTotal
                      )

    if instalacao == 'i':
        if qtDeWatts <= 5000:
            if qtDeWatts < 5000:
                consumoNormal = qtDeWatts
            else:
                consumoNormal = 5000

            valorPagarTotalNormal = qtDeWatts * vlIndustrial5000
            valorPagarTotal = valorPagarTotalNormal

            resultado(instalacao,
                      consumoNormal,
                      vlIndustrial5000,
                      valorPagarTotalNormal,
                      valorExcedente,
                      vlIndustrial5000ac,
                      valorPagarExc,
                      valorPagarTotal
                      )


        else:
            if qtDeWatts < 5000:
                consumoNormal = qtDeWatts
            else:
                consumoNormal = 5000

            valorPagarTotalNormal = qtDeWatts * vlIndustrial5000
            valorPagarTotal = valorPagarTotalNormal

            valorExcedente = qtDeWatts - 5000
            valorPagar5000 = 5000 * vlIndustrial5000
            valorPagarExc = valorExcedente * vlIndustrial5000ac
            valorPagarTotal = valorPagar5000 + valorPagarExc

            resultado(instalacao,
                      consumoNormal,
                      vlIndustrial5000,
                      valorPagar5000,
                      valorExcedente,
                      vlIndustrial5000ac,
                      valorPagarExc,
                      valorPagarTotal
                      )

    sair = input('Digite "S" para sair ou enter para continuar').lower()
    if sair == 's':
        break
