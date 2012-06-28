from tkinter import *
import modelo
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


def gera_senha():
    '''
    Alteração do valor exibido com nova senha randômica.
    '''
    nova_senha = modelo.Senha()
    senha.set(nova_senha.valor)

'''
Dois botoes, um para gerar a senha e um outro para sair do aplicativo.
'''
gera = Button(app, text="Gerar!", width=10, command=gera_senha)
gera.pack(side='left', padx=10, pady=10)

sair = Button(app, text="Sair", width=10, command=app.quit)
sair.pack(side='right', padx=10, pady=10)

app.mainloop()
