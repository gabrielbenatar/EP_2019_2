#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:13:48 2019

@author: gabrielsalvatorbenatar
"""
import random

#dinheiro = 100 
#while dinheiro > 0:
#    print("Você tem {0} dinheiros".format(dinheiro)) 
#    aposta = int(input("Digite sua aposta: "))
#    if aposta > dinheiro:
#        print("Você não tem dinheiro o suficiente")
#        continue
#    if aposta <= 0:
#        break

c_cartas = []#crupier / computador
u_cartas = []#usuario

#cartas do crupier
while len(c_cartas) != 2:
    c_cartas.append(random.randint(1,11))
    if len(c_cartas) == 2:
        print ('O crupier tem X e',c_cartas[0])
        
#cartas do jogador
while len(u_cartas) != 2:
    u_cartas.append(random.randint(1,11))
    if len(u_cartas) == 2:
        print ('Você tem {0} e {1}'.format(u_cartas[0],u_cartas[1]))

#soma das cartas do usuario/jogador
Soma_u = u_cartas[0] + u_cartas[1]
while Soma_u < 21:
    compra = str(input('Você quer comprar ou deixar? digite ("c" ou "d"): '))
    if compra == 'c':
        u_cartas.append(random.randint(1,11))
        print("Agora você tem um total de " + str(sum(u_cartas)) + "dessas cartas", u_cartas)
    else:
        print("O crupier tem um total de " + str(sum(c_cartas)) + "dessas cartas", c_cartas)
        print("Você tem um total de " + str(sum(u_cartas)) + "dessas cartas", u_cartas)

#soma das cartas do computador
Soma_c = c_cartas[0] + c_cartas[1]
if Soma_c == 21:
    print('O COMPUTADOR FEZ BLACKJACK! Você perdeu!')
elif Soma_c > 21:
    print('O computador estourou! Você ganhou!')
    