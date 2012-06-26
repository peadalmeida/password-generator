#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def extrai_conteudo(nome_arq):
    lista = []
    with open(nome_arq, 'r') as arq:
        for valor in arq:
            lista.append(valor.strip())
    return lista

lista_sub_fem = extrai_conteudo('sub_fem.txt')
lista_sub_mas = extrai_conteudo('sub_mas.txt')
lista_adj_mas = extrai_conteudo('adj_mas.txt')
lista_adj_fem = extrai_conteudo('adj_fem.txt')


class Senha:

    def __init__(self):
        self.valor = self.gera_senha()

    def gera_senha(self):
        genero = random.choice(['m', 'f'])
        if genero == 'm':
            return random.choice(lista_sub_mas) + \
                    random.choice(lista_adj_mas) + \
                    '{:03}'.format(random.choice(range(100)))
        else:
            return random.choice(lista_sub_fem) + \
                    random.choice(lista_adj_fem) + \
                    '{:03}'.format(random.choice(range(100)))
