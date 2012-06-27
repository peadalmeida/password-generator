from tkinter import *

app = Tk()
app.title("Gerador de Senhas")
app.geometry('500x200+300+200')

v = StringVar()
Label(app, textvariable=v, font=("Helvetica", 30)).pack()
v.set("Senha gerada aqui")

gera = Button(app, text="Gerar!", width=10)
gera.pack(side='left', padx=10, pady=10)

sair = Button(app, text="Sair", width=10, command=app.quit)
sair.pack(side='right', padx=10, pady=10)

app.mainloop()
