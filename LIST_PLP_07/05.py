''' -----------------------------------------------------------------
    UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
    Nome: Mauricio Silva Amaral
    RA : D92EJG-0
    Turma : CP6P01
    Data: 10/10/2021
    Lista: 07 - 05
    Enunciado: 05 – Defina uma função recursiva que calcule o
    maior divisor comum (M.D.C) entre dois números a e b, em
    que a > b.
    𝑚𝑑𝑐(𝑎, 𝑏) = {𝑎
    𝑚𝑑𝑐(𝑏, 𝑎 − 𝑏.[ 𝑎 𝑏])
    𝑏 = 0
    𝑎 > 𝑏

    Em que 𝑎 − 𝑏.[𝑎 𝑏 ] pode ser escrito em Python como: a%b
    ----------------------------------------------------------------- '''


def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b , a%b)

print(mdc(30, 12))
