from tkinter import *
from tkinter.messagebox import *
import random
import sys
import new_io as nio

'''Carrega substantivos e adjetivos oriundos de arquivos no momento
    em que módulo é importado.
    Também carregam as senhas já sorteadas.
    Em caso de falha o aplicativo é abortado.
'''
try:
    lista_sub_fem = nio.extrai_conteudo('arqs/sub_fem.txt')
    lista_sub_mas = nio.extrai_conteudo('arqs/sub_mas.txt')
    lista_adj_mas = nio.extrai_conteudo('arqs/adj_mas.txt')
    lista_adj_fem = nio.extrai_conteudo('arqs/adj_fem.txt')
    senhas_antigas = nio.extrai_conteudo('arqs/senhas_antigas.txt')
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
app.geometry('500x100+300+100')
app['background'] = '#333'
'''
Inicializaçao do texto onde será exibida a senha.
'''
senha = StringVar()
buffer_senhas = []
Label(app, textvariable=senha, font=("Helvetica", 30),
        background='#333',foreground='green').pack()
senha.set("Senha gerada aqui")


def nova_senha():
    '''
    Alteração do valor exibido com nova senha randômica.
    '''
    nova_senha = gera_senha()
    while nova_senha in senhas_antigas or nova_senha in buffer_senhas:
        nova_senha = gera_senha()
    senha.set(nova_senha)
    buffer_senhas.append(nova_senha)


def save_and_destroy():
    '''salva senhas antigas antes de destruir a aplicação'''
    nio.grava_conteudo(buffer_senhas, 'arqs/senhas_antigas.txt')
    app.destroy()

'''
Dois botoes, um para gerar a senha e um outro para sair do aplicativo.
'''
img_senha = PhotoImage(file='imgs/senha.gif')
gera = Button(app, text="Gerar!", command=nova_senha,
                        image=img_senha, compound='left')
gera.pack(side='left', padx=10, pady=10)

img_sair = PhotoImage(file='imgs/sair.gif')
sair = Button(app, text="Sair", command=save_and_destroy,
                        image=img_sair, compound='left')
sair.pack(side='right', padx=10, pady=10)

app.protocol("WM_DELETE_WINDOW", save_and_destroy)
app.mainloop()
