from tkinter import *

app = Tk()
app.title("Gerador de Senhas")
app.geometry('500x200+300+200')

v = StringVar()
Label(app, textvariable=v , font=("Helvetica",30)).pack()
v.set ("Senha gerada aqui")

Gera = Button(app, text = "Gerar!" , width = 10)
Gera.pack(side = 'left' , padx = 10 , pady = 10)

Sair = Button(app, text = "Sair", width = 10 , command=app.quit)
Sair.pack(side = 'right' , padx = 10 , pady = 10)

app.mainloop()

