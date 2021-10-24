""" -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 10/10/2021
    Lista: 07 - 06
    Enunciado: 6 – Usando a função mdc definida no exercício
    anterior, defina uma função para calcular o menor múltiplo
    comum (MMC) entre dois números.

    MMC(a,b) = { |a*b| / mdc(a,b)}


    Em que |a *b|  pode ser escrito em Python como; abs(a*b)
    ----------------------------------------------------------------- """


def mmc(a, b):
    def mdc(a, b):
        if b == 0:
            return a
        else:
            return mdc(b, a % b)

    valor = abs(a * b) / mdc(a, b)
    return valor


print(mmc(16, 40))
