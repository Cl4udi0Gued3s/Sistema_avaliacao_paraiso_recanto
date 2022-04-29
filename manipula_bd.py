# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 17:58:16 2022

@author: claud
"""

'''
Manipulação do banco de dados
'''

import pandas as pd
tabela = pd.read_csv('diretorio da planilha')

#Avaliação garçons

def avaliagarcom(nome):
    
    garcom = tabela['Garçom']
    avaliacaogarcom = tabela['Avaliação do garçom']
    garcom = list(garcom)
    avaliacaogarcom = list(avaliacaogarcom)



    del(garcom[0])
    del(avaliacaogarcom[0])
    
    lista_garcom = []
    c=1
        
    for i in garcom:
        i = i.title()
        lista_garcom.append(i)
        c+=1
    
    tamanho_garcom = len(garcom)
    
    lista_nome_pessimo = []
    lista_nome_ruim = []
    lista_nome_regular = []
    lista_nome_bom = []
    lista_nome_excelente = []
    
    
    c = 0
    while c < tamanho_garcom:
        
        if lista_garcom[c] == nome and avaliacaogarcom[c] =='Péssimo':
            lista_nome_pessimo.append('sim')
        elif lista_garcom[c] == nome and avaliacaogarcom[c] =='Ruim':
            lista_nome_ruim.append('sim')
        elif lista_garcom[c] == nome and avaliacaogarcom[c] =='Regular':
            lista_nome_regular.append('sim')
        elif lista_garcom[c] == nome and avaliacaogarcom[c] =='Bom':
            lista_nome_bom.append('sim')
        elif lista_garcom[c] == nome and avaliacaogarcom[c] =='Excelente':
            lista_nome_excelente.append('sim')
            
        c+=1
        
        
    nome_pessimo = len(lista_nome_pessimo)
    nome_ruim = len(lista_nome_ruim)
    nome_regular = len(lista_nome_regular)
    nome_bom = len(lista_nome_bom)
    nome_excelente = len(lista_nome_excelente)
    
    print(f'Qualidade de atendimento do {nome}')
    print()
    print(f'{nome} possui {nome_pessimo} Péssimos')
    print(f'{nome} possui {nome_ruim} Ruins')
    print(f'{nome} possui {nome_regular} Regulares')
    print(f'{nome} possui {nome_bom} Bons')
    print(f'{nome} possui {nome_excelente} Excelentes')
    print('-------------------------------------------')
    
    soma = nome_pessimo + nome_ruim + nome_regular + nome_bom + nome_excelente
    
    print(f'Péssimo representa {(nome_pessimo / soma ) * 100}%')
    print(f'Ruim representa {(nome_ruim / soma ) * 100}%')
    print(f'Regular representa {(nome_regular / soma ) * 100}%')
    print(f'Bom representa {(nome_bom / soma ) * 100}%')
    print(f'Excelente representa {(nome_excelente / soma ) * 100}%')
    

avaliagarcom(input('Digite o nome do garçom: ').title())   
#-----------------------------------------------------------------------------

#avaliaçao comida

def avaliacomida(argumento):
    
    if argumento == 'ok':
        
    
        qualidade_comida = tabela['Avaliação da comida']
        qualidade_comida = list(qualidade_comida)
        
        del(qualidade_comida[0])
        
        tamanho_comida = len(qualidade_comida)
        
        lista_comida_pessimo = []
        lista_comida_ruim = []
        lista_comida_regular = []
        lista_comida_bom = []
        lista_comida_excelente = []
        
        c = 0
        while c < tamanho_comida:
            
            if qualidade_comida[c] == 'Péssima':
                lista_comida_pessimo.append('sim')
            elif qualidade_comida[c] == 'Ruim':
                lista_comida_ruim.append('sim')
            elif qualidade_comida[c] == 'Regular':
                lista_comida_regular.append('sim')
            elif qualidade_comida[c] == 'Boa':
                lista_comida_bom.append('sim')
            elif qualidade_comida[c] == 'Excelente':
                lista_comida_excelente.append('sim')
                
            c+=1
            
            
        comida_pessimo = len(lista_comida_pessimo)
        comida_ruim = len(lista_comida_ruim)
        comida_regular = len(lista_comida_regular)
        comida_bom = len(lista_comida_bom)
        comida_excelente = len(lista_comida_excelente)
        
        print('Qualidade da comida')
        print()
        print(f'A qualidade da comida possui {comida_pessimo} Péssimos')
        print(f'A qualidade da comida possui {comida_ruim} Ruins')
        print(f'A qualidade da comida possui {comida_regular} Regulares')
        print(f'A qualidade da comida possui {comida_bom} Bons')
        print(f'A qualidade da comida possui {comida_excelente} Excelentes')
        print('-------------------------------------------------------------')
        
        soma = comida_pessimo + comida_ruim + comida_regular + comida_bom + comida_excelente
        
        print(f'Péssimo representa {(comida_pessimo / soma ) * 100}%')
        print(f'Ruim representa {(comida_ruim / soma ) * 100}%')
        print(f'Regular representa {(comida_regular / soma ) * 100}%')
        print(f'Bom representa {(comida_bom / soma ) * 100}%')
        print(f'Excelente representa {(comida_excelente / soma ) * 100}%')

avaliacomida(input('Digite ok para iniciar: '))

#-------------------------------------------------------------------
#Avaliação tempo de espera

def avaliatempo(argumento):
    
    if argumento == 'ok':
        
    
        tempo_comida = tabela['Tempo de espera']
        tempo_comida = list(tempo_comida)
        
        del(tempo_comida[0])
        
        tamanho_tempo = len(tempo_comida)
        
        lista_tempo_md = []
        lista_tempo_aceitavel = []
        lista_tempo_rapido = []
        lista_tempo_mr = []
        
        c = 0
        while c < tamanho_tempo:
            
            if tempo_comida[c] == 'Muito demorado':
                lista_tempo_md.append('sim')
            elif tempo_comida[c] == 'Aceitavel':
                lista_tempo_aceitavel.append('sim')
            elif tempo_comida[c] == 'Rapido':
                lista_tempo_rapido.append('sim')
            elif tempo_comida[c] == 'Muito rapido':
                lista_tempo_mr.append('sim')
                
            c+=1
            
            
        tempo_md = len(lista_tempo_md)
        tempo_aceitavel = len(lista_tempo_aceitavel)
        tempo_rapido = len(lista_tempo_rapido)
        tempo_mr = len(lista_tempo_mr)
        
        print('Tempo de espera pela comida')
        print()
        print(f'O tempo de espera pela comida possui {tempo_md} Muito demorado')
        print(f'A qualidade da comida possui {tempo_aceitavel} Aceitável')
        print(f'A qualidade da comida possui {tempo_rapido} Rápido')
        print(f'A qualidade da comida possui {tempo_mr} Muito rápido')
        print('-------------------------------------------------------------')
        
        soma = tempo_md + tempo_aceitavel + tempo_rapido + tempo_mr 
        
        print(f'Muito demorado representa {(tempo_md / soma ) * 100}%')
        print(f'Aceitável representa {(tempo_aceitavel / soma ) * 100}%')
        print(f'Rápido representa {(tempo_rapido / soma ) * 100}%')
        print(f'Muito rápido representa {(tempo_mr / soma ) * 100}%')

avaliatempo(input('Digite ok para iniciar: '))

#----------------------------------------------------------------------------
#Avaliação média de satisfação

def avalia_satisfacao(argumento):
    
    if argumento == 'ok':
        
        satisfacao = tabela['Satisfação']
        satisfacao = list(satisfacao)
        del(satisfacao[0])
        
        lista = []
        
        for i in satisfacao:
            i = i.replace(',','.')
            i = float(i)
            lista.append(i)
            
        media = sum(lista) / len(lista)
        print(f'O nível de satisfação total está em {media}%')
        
avalia_satisfacao(input('Digite ok para iniciar: '))
        
