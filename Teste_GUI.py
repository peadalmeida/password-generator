from tkinter import *

app = Tk()
app.title("Gerador de Senhas")
app.geometry('500x200+300+200')

Gera = Button(app, text = "Gerar!" , width = 10)
Gera.pack(side = 'left' , padx = 10 , pady = 10)

Sair = Button(app, text = "Sair", width = 10)
Sair.pack(side = 'right' , padx = 10 , pady = 10)

app.mainloop()

