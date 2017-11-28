#!/usr/bin/python
#-*-coding: utf-8 -*-
#Criado por GleisonJSilva
#Criado em : 28/11/2017, 16:12:36

from Dispositivo import Dispositivo
from tkinter import *
   
class AddDispositivo:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")   
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
  
        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()
   
        self.lbliddispositivo = Label(self.container2, text="idDispositivo:", font=self.fonte, width=10)
        self.lbliddispositivo.pack(side=LEFT)
  
        self.txtiddispositivo = Entry(self.container2)
        self.txtiddispositivo["width"] = 10
        self.txtiddispositivo["font"] = self.fonte
        self.txtiddispositivo.pack(side=LEFT)
   
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarDispositivo
        self.btnBuscar.pack(side=RIGHT)
   
        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
  
        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)
  
        self.lblmac = Label(self.container4, text="Mac:", font=self.fonte, width=10)
        self.lblmac.pack(side=LEFT)
   
        self.txtmac = Entry(self.container4)
        self.txtmac["width"] = 25
        self.txtmac["font"] = self.fonte
        self.txtmac.pack(side=LEFT)
   
        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirDispositivo
        self.bntInsert.pack (side=LEFT)
   
        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarDispositivo
        self.bntAlterar.pack (side=LEFT)
   
        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirDispositivo
        self.bntExcluir.pack(side=LEFT)
  
        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
        
    def inserirDispositivo(self):
        disp = Dispositivo()
        disp.nome = self.txtnome.get()
        disp.mac = self.txtmac.get()
        
        
        self.lblmsg["text"] = disp.insertDispositivo()   
        self.txtiddispositivo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtmac.delete(0, END)
         
        
    def alterarDispositivo(self):
        disp = Dispositivo()   
        disp.iddispositivo = self.txtiddispositivo.get()
        disp.nome = self.txtnome.get()
        disp.mac = self.txtmac.get()
        
   
        self.lblmsg["text"] = disp.updateDispositivo()
   
        self.txtiddispositivo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtmac.delete(0, END)
           
   
   
    def excluirDispositivo(self):
        disp = Dispositivo()   
        disp.iddispositivo = self.txtiddispositivo.get()   
        self.lblmsg["text"] = disp.deleteDispositivo()   
        self.txtiddispositivo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtmac.delete(0, END)
        
      
    def buscarDispositivo(self):
        disp = Dispositivo()   
        iddispositivo = self.txtiddispositivo.get()
   
        self.lblmsg["text"] = disp.selectDispositivo(iddispositivo)
   
        self.txtiddispositivo.delete(0, END)
        self.txtiddispositivo.insert(INSERT, disp.iddispositivo)
   
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, disp.nome)
   
        self.txtmac.delete(0, END)
        self.txtmac.insert(INSERT,disp.mac)
     
   
root = Tk()
AddDispositivo(root)
root.mainloop()