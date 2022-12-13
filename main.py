from random import choice
from nai import escolhas, color
from time import sleep


baralho = [[x for x in range(13)], [x for x in range(13)],[x for x in range(13)],[x for x in range(13)]]
naip = [0, 1, 2, 3]

jogador = [[], [], []]
compu = [[], [], []]

i = 0
u = 1

print(f"{'BLACKJACK':.^35}")

print("O crupiêr está embaralhando as cartas")
for escolha in range(4):
    naipesc = choice(naip)
    cartaesc = choice(baralho[naipesc])
    baralho[naipesc].remove(cartaesc)
    if escolha == 0 or escolha == 2:
        escolhas(jogador, cartaesc, naipesc)
        sleep(2)
        print(f"\n{i+1}º carta do jogador: {jogador[2][i]} de {jogador[1][i]}")
        i += 1
    if escolha == 1:
        escolhas(compu, cartaesc, naipesc)
        sleep(2)
        print(f"\n1º carta do crupiêr: {compu[2][i-1]} de {compu[1][i-1]}")
    if escolha == 3:
        escolhas(compu, cartaesc, naipesc)
        sleep(2)
        print("\n2º carta do crupiêr: Oculta")

if "Ás" in jogador[2] and "Valete" in jogador[2] or "Dama" in jogador[2] and "Ás" in jogador[2] \
        or "Rei" in jogador[2] and "Ás" in jogador[2]:
    jogador[0].clear()
    jogador[0].append(21)
    print("Você Fez 21!!!")

print("."*35)

while True:
    if sum(jogador[0]) >= 21:
        break
    print(f"\nAté aqui você tem {len(jogador[0])} cartas,\nno total de {sum(jogador[0])}.")
    cont = int(input("\nQuer mais carta? 1[sim] 2[nao]: "))
    print("." * 35)
    while cont != 1 and cont != 2:
        print("Informe uma opção válida")
        cont = int(input("Quer mais carta? 1[sim] 2[nao]: "))
    if cont == 2:
        break
    naipesc = choice(naip)
    cartaesc = choice(baralho[naipesc])
    baralho[naipesc].remove(cartaesc)
    escolhas(jogador, cartaesc, naipesc)
    sleep(2)
    print(f"\n{i + 1}º carta do jogador: {jogador[2][i]} de {jogador[1][i]}")
    i += 1

print("." * 35)
sleep(2)

print(f"\n2º carta do crupier revelada: {compu[2][u]} de {compu[1][u]}")

if "Ás" in compu[2] and "Valete" in compu[2] or "Dama" in compu[2] and "Ás" in compu[2] \
        or "Rei" in compu[2] and "Ás" in compu[2]:
    compu[0].clear()
    compu[0].append(21)

print(f"\nNo total de {sum(compu[0])}")

u += 1

print("."*35)


while sum(compu[0]) < sum(jogador[0]) <= 21:
    print("Crupiêr vai pegar mais uma carta")
    naipesc = choice(naip)
    cartaesc = choice(baralho[naipesc])
    baralho[naipesc].remove(cartaesc)
    escolhas(compu, cartaesc, naipesc)
    sleep(3)
    print(f"\n{u+1}º carta do crupier revelada: {compu[2][u]} de {compu[1][u]}\nNo total de {sum(compu[0])}")
    u += 1
    print("." * 35)

if sum(compu[0]) > 21 and sum(jogador[0]) <=21:
    print(color("Você ganhou!!", "green"))
if sum(jogador[0]) > 21 or 21 >= sum(compu[0]) > sum(jogador[0]):
    if sum(jogador[0]) > 21:
        print(color("\nVocê passou de 21\nVOCê PERDEU!!!", "red"))
    else:
        print(color("\nCrupier fez 21 ou chegou mais perto do que você\nVOCê PERDEU!!!", "red"))
if sum(compu[0]) == 21 == sum(jogador[0]) and compu[0] == jogador[0]:
    print(color("Empate", "yellow"))
























