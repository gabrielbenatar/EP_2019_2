#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:13:48 2019

@author: gabrielsalvatorbenatar
"""
import random


c_cartas = []#crupier / computador
u_cartas = []#usuario

#cartas do crupier
while len(c_cartas) != 2:
    c_cartas.append(random.randint(1,11))
    if len(c_cartas) == 2:
        print ('O crupier tem:',c_cartas)


