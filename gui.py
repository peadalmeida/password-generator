from tkinter import *
import modelo

app = Tk()
app.title("Gerador de Senhas")
app.geometry('500x200+300+200')

senha = StringVar()
Label(app, textvariable=senha, font=("Helvetica", 30)).pack()
senha.set("Senha gerada aqui")


def gera_senha():
    nova_senha = modelo.Senha()
    senha.set(nova_senha.valor)

gera = Button(app, text="Gerar!", width=10, command=gera_senha)
gera.pack(side='left', padx=10, pady=10)

sair = Button(app, text="Sair", width=10, command=app.quit)
sair.pack(side='right', padx=10, pady=10)

app.mainloop()
