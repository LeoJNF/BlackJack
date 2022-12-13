from random import choice


def naipes(carta):
    if carta == 0:
        return "paus"
    elif carta == 1:
        return "espadas"
    elif carta == 2:
        return "ouros"
    elif carta == 3:
        return "copas"


def nome(carta):
    if carta == 0:
        return "Ás"
    elif carta == 1:
        return "Valete"
    elif carta == 11:
        return "Dama"
    elif carta == 12:
        return "Rei"
    else:
        return carta


def valoreal(carta):
    if carta == 0:
        return 1
    if carta == 1:
        return 10
    if carta == 11:
        return 10
    if carta == 12:
        return 10
    else:
        return carta


def escolhas(lista, c, d):
    lista[0].append(valoreal(c))
    lista[1].append(naipes(d))
    lista[2].append(nome(c))


def color(texto, cor):
    if cor == 'red':
        return f'\033[31m{texto}\033[m'
    if cor == 'green':
        return f'\033[32m{texto}\033[m'
    if cor == 'yellow':
        return f'\033[33m{texto}\033[m'