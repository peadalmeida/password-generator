import random


def extrai_conteudo(nome_arq):
    '''
       Abre um arquivo de nome nome_arq e retorna uma lista
       com as linhas do arquivo.
    '''
    lista = []
    with open(nome_arq, 'r') as arq:
        for valor in arq:
            lista.append(valor.strip())
    return lista


'''Carrega substantivos e adjetivos oriundos de arquivos no momento
    em que módulo é importado.
'''
lista_sub_fem = extrai_conteudo('sub_fem.txt')
lista_sub_mas = extrai_conteudo('sub_mas.txt')
lista_adj_mas = extrai_conteudo('adj_mas.txt')
lista_adj_fem = extrai_conteudo('adj_fem.txt')


class Senha:
    '''Classe representando uma nova senha gerada aleatoriamente.'''
    def __init__(self):
        '''
            Inicializador com atribuição de valor aleatório.
        '''
        self.valor = self.gera_senha()

    def gera_senha(self):
        '''
            Retorna a concatenação de um substantivo com um adjetivo e um
            número de três digitos(0,100).
            O adjetivo concorda em gênero com o substantivo.
            Exemplo:
                >>>gera_senha()
                   portamagra001
                >>>gera_senha()
                   homemgordo084

        '''
        genero = random.choice(['m', 'f'])
        if genero == 'm':
            return random.choice(lista_sub_mas) + \
                    random.choice(lista_adj_mas) + \
                    '{:03}'.format(random.choice(range(101)))
        else:
            return random.choice(lista_sub_fem) + \
                    random.choice(lista_adj_fem) + \
                    '{:03}'.format(random.choice(range(101)))
