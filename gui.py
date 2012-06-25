#coding: utf-8
#Autor:Cassio
#Programa desenvolvido utilizando Python 3.2.3
#
#Programa para demonstrar a simplicidade de uma interface gráfica utilizando
#utilizando tkinter
#
from tkinter import *


class Janela_Principal:

    def __init__(self, master):
        master.geometry('100x100')
        self.frame = Frame(master)
        self.frame.pack()
        self.button = Button(self.frame, text='Sair', fg="red",
                command=self.frame.quit)
        self.button.pack(padx=10, pady=30)
        
class Controle:
	
	def __init__(self):
		self.root = Tk()
		self.app = Janela_Principal(self.root)
		self.root.mainloop()

controle = Controle();
