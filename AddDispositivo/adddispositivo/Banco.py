#!/usr/bin/python
#-*-coding: utf-8 -*-
#Criado por GleisonJSilva
#Criado em : 28/11/2017, 16:14:26

import psycopg2

class Banco():

    def __init__(self):
        self.con = psycopg2.connect(host='localhost', database='postgres',user = 'gleisongjs', password = 'jsilva996') #DB no Asus
        #self.con = psycopg2.connect(host='localhost', database='dispositivo',user = 'gleisongjs', password = 'jsilva996')#Db do Servidor