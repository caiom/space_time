#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:14:30 2020

@author: caiom
"""

import numpy as np

def flood_fill(mapa, initial_y, initial_x, fill_value=2, target_value=1):
    '''Dado uma semente na posicao (initial_y, initial_x) e um mapa
    2D binario em numpy (int64) a funcao procura por todos os vizinhos 
    4-conectados que possuam o valor target_value e troca seus 
    valores por fill_value (in-place). Alem disso, a funcao retorna o 
    numero de vizinhos encontrados.
    '''
    
    assert fill_value != target_value, 'Target and fill value must be different'
    
    height, width = mapa.shape[:2]
    
    # Variavel que guarda todas as posicoes que devem ser checadas
    queue = [(initial_y, initial_x)]
    
    found_number = 0
    
    # Enquanto ainda existir uma posicao a checar
    while len(queue):
        
        y, x = queue.pop()
        
        # A posicao atual eh valida?
        if y > (height - 1) or x > (width - 1):
            continue
        
        if y < 0 or x < 0:
            continue
        
        if mapa[y, x] != target_value:
            continue
        
        mapa[y, x] = fill_value
        found_number += 1
        
        # Adicona os 4 vizinhos para checagem
        queue.append((y+1, x))
        queue.append((y, x+1))
        queue.append((y-1, x))
        queue.append((y, x-1))
        
    return found_number
        
def numero_ilhas(mapa):
    '''Devolve o numero de ilhas no mapa (considere vizinhança 4-conexa)'''
    
    mapa_np = np.atleast_2d(mapa)
    # Comparacao de float eh problematica
    mapa_np = mapa_np.astype(np.int64)
    
    height, width = mapa_np.shape[:2]
    
    nr_ilhas = 0
    
    for i in range(height):
        for j in range(width):
            
            if mapa_np[i, j] == 1:
                flood_fill(mapa_np, i, j, 0)
                nr_ilhas += 1
                
    return nr_ilhas
            
            
            
def quantidade_de_terra_afetada(mapa, i, j):
    '''Calcula o numero de pontos de solo do mapa que podem ser afetados por uma 
    semente lançada em mapa[i, j] (considere vizinhança 4-conexa)'''
    
    mapa_np = np.atleast_2d(mapa)
    # Comparacao de float eh problematica
    mapa_np = mapa_np.astype(np.int64)
    
    return flood_fill(mapa_np, i, j, 2)
    
    
    
mapa = [[ 0., 0., 0., 0., 0., 0.],
    [ 0., 0., 0., 0., 0., 0.],
    [ 0., 1., 1., 1., 0., 0.],
    [ 0., 0., 1., 0., 1., 0.],
    [ 0., 0., 0., 0., 1., 0.],
    [ 0., 0., 0., 0., 0., 0.]]

print(numero_ilhas(mapa))
print(quantidade_de_terra_afetada(mapa, 0, 0))
print(quantidade_de_terra_afetada(mapa, 2, 2))

