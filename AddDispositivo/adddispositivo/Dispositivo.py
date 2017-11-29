#!/usr/bin/python
#-*-coding: utf-8 -*-
#Criado por GleisonJSilva
#Criado em : 28/11/2017, 16:18:18

from Banco import Banco

class Dispositivo(object):
    
    def __init__(self, iddispositivo = 0, nome = "", mac = ""):
        self.info = {}
        self.iddispositivo = iddispositivo
        self.nome = nome
        self.mac = mac
        
        
    def insertDispositivo(self):
        
        banco = Banco()       
                
        try:            
            c = banco.con.cursor()
            c.execute("insert into mac (nome, mac) values ('"+ self.nome +"', '"+ self.mac +"')")
            banco.con.commit()
            c.close()
            return "Dispositivo cadastrado com sucesso!"
        
        except:
            return "Ocorreu um erro na inserção do dispositivo"
    
    
    def updateDispositivo(self):
        banco = Banco()
        try:
   
            c = banco.con.cursor()
   
            c.execute("update mac set nome = '" + self.nome + "', mac = '" + self.mac + "' where id = " + self.iddispositivo + " ")
   
            banco.con.commit()
            c.close()
   
            return "Dispositivo atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do dispositivo"
   
    def deleteDispositivo(self):
   
        banco = Banco()
        try:
   
            c = banco.con.cursor()
   
            c.execute("delete from mac where id = " + self.iddispositivo + " ")
   
            banco.con.commit()
            c.close()
   
            return "Dispositivo excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do dispositivo"
   
    def selectDispositivo(self, iddispositivo):
        banco = Banco()
        try:  
            c = banco.con.cursor()   
            c.execute("select * from mac where id = " + iddispositivo + "  ")
            
            for linha in c:
                self.iddispositivo = linha[0]
                self.mac = linha[1]
                self.nome = linha[2]
                
            c.close()   
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"