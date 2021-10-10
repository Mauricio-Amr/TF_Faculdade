''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 09/10/2021
    Lista: 02 - 08
    Enunciado: 08 – Escreva um programa que leia um valor em metros e o exiba convertido em milímetros. 1 metro é igual
    a 100 cm que é igual a 10 mm.
    ----------------------------------------------------------------- '''

converterCm = 100
converterMm = 1000

try:
    valorMetro = float(input("Digite o valor em metros : "))

    valorConvertidoCm = valorMetro * converterCm
    valorConvertidoMm = valorMetro * converterMm

    print(f'\nvalor : {valorMetro} \nConvertido em Cm : {valorConvertidoCm} \nConvertido em Mm : {valorConvertidoMm}')

except:
    print("Valor digitado não correspode a um numero")