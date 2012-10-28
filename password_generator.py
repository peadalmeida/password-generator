#-*-coding:utf:8 -*-
#Tabalho de Linguagens de Programação I
#Professor : Bruno Schneider
#
#Alunos: Cássio Botaro, Pedro Augusto Almeida
#Turma: 10 A

from tkinter import Tk, StringVar, Button, PhotoImage, Label
from tkinter.messagebox import showwarning
from random import choice
from sys import exit


def extrair_conteudo(caminho_arquivo):
    '''Extrai conteudo de arquivo cujo caminho é passado.
    O retorno da função é uma lista com todas as linhas do arquivo'''
    with open(caminho_arquivo) as arq:
        lista = arq.read().strip().split('\n')
    return lista

'''Carrega substantivos e adjetivos oriundos de arquivos no momento
    em que módulo é importado.
    Em caso de falha o aplicativo é abortado.
'''
try:
    lista_sub_fem = extrair_conteudo('arqs/sub_fem.txt')
    lista_sub_mas = extrair_conteudo('arqs/sub_mas.txt')
    lista_adj_mas = extrair_conteudo('arqs/adj_mas.txt')
    lista_adj_fem = extrair_conteudo('arqs/adj_fem.txt')
except IOError as exc:
    showwarning('Error!', 'Erro de arquivo:' + str(exc))
    exit(1)
except Exception as exc:
    showwarning('Error!', exc)
    exit(1)


def gerar_senha():
    '''
    Retorna a concatenação de um substantivo com um adjetivo e um
    número de três digitos(0,100).
    O adjetivo concorda em gênero com o substantivo.
    Exemplo:
        >>>gerar_senha()
           portamagra001
        >>>gerar_senha()
           homemgordo084

    '''
    genero = choice(('m', 'f'))
    if genero == 'm':
        return choice(lista_sub_mas) + \
            choice(lista_adj_mas) + \
            '{:03}'.format(choice(range(101)))
    else:
        return choice(lista_sub_fem) + \
            choice(lista_adj_fem) + \
            '{:03}'.format(choice(range(101)))


def gerar_multiplas_senhas(num_senhas=10):
    '''Gera uma lista de senhas com num_senhas elementos.'''
    return [gerar_senha() for _ in range(num_senhas)]

if __name__ == '__main__':

    def modificar_senha():
        '''
        Alteração do valor exibido com nova senha randômica.
        '''
        senha.set(gerar_senha())

    '''Inicialização da tela  com dimensionamento, definição de cor e
       outras características.'''
    app = Tk()
    app.title("Gerador de Senhas")
    app.geometry('500x100')
    '''Desativa redimensionamento da tela'''
    app.resizable(0, 0)
    app['background'] = '#333'
    '''
    Inicializaçao do texto onde será exibida a senha.
    '''
    senha = StringVar()
    Label(app, textvariable=senha, font=("Helvetica", 30), background='#333',
          foreground='green').pack()
    senha.set("Senha gerada aqui")
    '''
    Dois botões, um para gerar a senha e um outro para sair do aplicativo.
    '''
    img_senha = PhotoImage(file='imgs/senha.gif')
    gera = Button(app, text="Gerar!", command=modificar_senha,
                  image=img_senha, compound='left')
    gera.pack(side='left', padx=10, pady=10)

    img_sair = PhotoImage(file='imgs/sair.gif')
    sair = Button(app, text="Sair", command=app.quit,
                  image=img_sair, compound='left')
    sair.pack(side='right', padx=10, pady=10)
    '''Inicia loop de eventos'''
    app.mainloop()
