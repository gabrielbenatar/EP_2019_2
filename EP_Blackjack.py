#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:13:48 2019

@author: gabrielsalvatorbenatar
"""
import random
dinheiro = 100 

c_cartas = []#crupier / computador
u_cartas = []#usuario


Soma_u = sum(u_cartas)#soma das cartas do usuario/jogador

Soma_c = sum(c_cartas)#soma das cartas do computador



   
while dinheiro > 0:
    print("Você tem {0} dinheiros".format(dinheiro)) 
    aposta = int(input("Quanto você quer apostar? "))
    if aposta <= 0:
        print("Aposta invalida")
        aposta = int(input("Quanto você quer apostar? "))
    
    if aposta > dinheiro:
        print("Aposte um valor menor")
        aposta = int(input("Quanto você quer apostar? "))
    
    #cartas do crupier    
    while len(c_cartas) != 2:
        c_cartas.append(random.randint(1,11))
        if len(c_cartas) == 2:
            print ('O crupier tem X e',c_cartas[0])
#        if sum(c_cartas) < 17:
#            c_cartas.append(random.randint(1,11))
            
        elif Soma_c == 21:
            print('O COMPUTADOR FEZ BLACKJACK! Você perdeu!')
            dinheiro -= aposta
            break
        
        elif Soma_c > 21:
            print('O computador estourou! Você ganhou!')
            dinheiro += aposta
            break

    #cartas do jogador
    while len(u_cartas) != 2:
        u_cartas.append(random.randint(1,11))
        if len(u_cartas) == 2:
            print ('Você tem {0} e {1}'.format(u_cartas[0],u_cartas[1]))
   
    Soma_u = sum(u_cartas)#soma das cartas do usuario/jogador
    Soma_c = sum(c_cartas)#soma das cartas do computador

    while Soma_u < 21:   
        compra = str(input('Você quer comprar ou deixar? '))
        if compra != "comprar" and compra != "deixar":
            print("Digite novamente")
            compra = str(input('Você quer comprar ou deixar? '))
        
        if compra == 'comprar':
            u_cartas.append(random.randint(1,11))
            print("Agora você tem um total de " + str(sum(u_cartas)) + " dessas cartas", u_cartas)
            
            if sum(u_cartas) > 21:
                print('ESTOUROU! PERDEU')
                dinheiro -=aposta
                
                break
            
            if sum(u_cartas) == 21:
                print("VOCÊ FEZ BLACKJACK! Você ganhou!")
                dinheiro += aposta * 1.5
                print("Você tem {0} dinheiros".format(dinheiro))
                break
        
        
        else:
            print("O crupier tem um total de " + str(sum(c_cartas)) + " dessas cartas", c_cartas)
            print("Você tem um total de " + str(sum(u_cartas)) + " dessas cartas", u_cartas)
            if sum(u_cartas) > sum(c_cartas):
                print("Você Ganhou! :) ")
                dinheiro += aposta
                print("Você tem {0} dinheiros".format(dinheiro))
                break
            else:
                print("Você Perdeu :( ")
                dinheiro -= aposta
                break
            
            
            
#  ==== =====    ======   ======   ======   =======    =======    =======    ========    ========    ===========  ======= =====              
            
            
    continuacao = input("Você quer continuar jogando?")
    if continuacao == "sim" or continuacao == "Sim":
       
       
        while dinheiro > 0:
            c_cartas = []#crupier / computador
            u_cartas = []#usuario
            print("Você tem {0} dinheiros".format(dinheiro)) 
            aposta = int(input("Quanto você quer apostar? "))
            if aposta <= 0:
                print("Aposta invalida")
                aposta = int(input("Quanto você quer apostar? "))
            
            if aposta > dinheiro:
                print("Aposte um valor menor")
                aposta = int(input("Quanto você quer apostar? "))
            
            #cartas do crupier    
            while len(c_cartas) != 2:
                c_cartas.append(random.randint(1,11))
                if len(c_cartas) == 2:
                    print ('O crupier tem X e',c_cartas[0])
#                if sum(c_cartas) < 17:
#                    c_cartas.append(random.randint(1,11))
                    
                elif Soma_c == 21:
                    print('O COMPUTADOR FEZ BLACKJACK! Você perdeu!')
                    dinheiro -= aposta
                    break
                
                elif Soma_c > 21:
                    print('O computador estourou! Você ganhou!')
                    dinheiro += aposta
                    break
        
            #cartas do jogador
            while len(u_cartas) != 2:
                u_cartas.append(random.randint(1,11))
                if len(u_cartas) == 2:
                    print ('Você tem {0} e {1}'.format(u_cartas[0],u_cartas[1]))
           
            Soma_u = sum(u_cartas)#soma das cartas do usuario/jogador
            Soma_c = sum(c_cartas)#soma das cartas do computador
        
            while Soma_u < 21:   
                compra = str(input('Você quer comprar ou deixar? '))
                if compra != "comprar" and compra != "deixar":
                    print("Digite novamente")
                    compra = str(input('Você quer comprar ou deixar? '))
                
                if compra == 'comprar':
                    u_cartas.append(random.randint(1,11))
                    print("Agora você tem um total de " + str(sum(u_cartas)) + " dessas cartas", u_cartas)
                    
                    if sum(u_cartas) > 21:
                        print('ESTOUROU! PERDEU')
                        dinheiro -=aposta
                        print("Você tem {0} dinheiros".format(dinheiro))
                        
                        break
                    
                    if sum(u_cartas) == 21:
                        print("VOCÊ FEZ BLACKJACK! Você ganhou!")
                        dinheiro += aposta * 1.5
                        print("Você tem {0} dinheiros".format(dinheiro))
                        break
                
                
                else:
                    print("O crupier tem um total de " + str(sum(c_cartas)) + " dessas cartas", c_cartas)
                    print("Você tem um total de " + str(sum(u_cartas)) + " dessas cartas", u_cartas)
                    if sum(u_cartas) > sum(c_cartas):
                        print("Você Ganhou! :) ")
                        dinheiro += aposta
                        print("Você tem {0} dinheiros".format(dinheiro))
                        break
                    else:
                        print("Você Perdeu :( ")
                        dinheiro -= aposta
                        print("Você tem {0} dinheiros".format(dinheiro))
                        break
                
    elif continuacao == "não" or continuacao == "Não":
        print("FIM")
        a = False
        break
    
    
