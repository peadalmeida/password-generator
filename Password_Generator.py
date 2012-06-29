from tkinter import *
from tkinter.messagebox import *
import random
import sys


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
    Em caso de falha o aplicativo é abortado.
'''
try:
    lista_sub_fem = extrai_conteudo('sub_fem.txt')
    lista_sub_mas = extrai_conteudo('sub_mas.txt')
    lista_adj_mas = extrai_conteudo('adj_mas.txt')
    lista_adj_fem = extrai_conteudo('adj_fem.txt')
except Exception as exc:
    showwarning('Error!', exc)
    sys.exit(1)


def gera_senha():
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

'''
Cria-se uma janela com o titulo "Gerador de Senhas"
e as devidas dimensões
'''
app = Tk()
app.title("Gerador de Senhas")
app.geometry('500x200+300+200')

'''
Inicializaçao do texto onde será exibida a senha.
'''
senha = StringVar()
Label(app, textvariable=senha, font=("Helvetica", 30)).pack()
senha.set("Senha gerada aqui")


def nova_senha():
    '''
    Alteração do valor exibido com nova senha randômica.
    '''
    senha.set(gera_senha())

'''
Dois botoes, um para gerar a senha e um outro para sair do aplicativo.
'''
gera = Button(app, text="Gerar!", width=10, command=nova_senha)
gera.pack(side='left', padx=10, pady=10)

sair = Button(app, text="Sair", width=10, command=app.quit)
sair.pack(side='right', padx=10, pady=10)

app.mainloop()
