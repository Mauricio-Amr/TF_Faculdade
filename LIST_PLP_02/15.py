''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 09/10/2021
    Lista: 02 - 15
    Enunciado: 15 – Escreva um programa para calcular a redução do tempo
    de vida de um fumante. Pergunte a quantidade de cigarros fumados por
    dia e quantos anos ela já fumou. Considere que um fumante perde 10
    minutos de vida a cada cigarro e calcule quantos dias de vida um
    fumante perderá. Exiba o total em dias.
    ----------------------------------------------------------------- '''


quantidadeDeAnos = int(input("Digite a quantos anos você fuma : "))
quantidadesDeCigarros = int(input("Digite quntos cigarro vc fuma por dia : "))

#Tempo decomposto
cigarro = 10
diasnoano = 365
dia = 24*60


#retorna o tempo fumando ate agorac

tempoFumado = quantidadesDeCigarros * cigarro
converteAnoDia = quantidadeDeAnos * diasnoano
vidaPerdida = tempoFumado*converteAnoDia
diasPerdidos = vidaPerdida / dia


print(f'Voce perdeu {diasPerdidos:.1f} dias fumando ')