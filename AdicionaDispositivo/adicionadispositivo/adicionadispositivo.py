#!/usr/bin/python
#-*-coding: utf-8 -*-
#Criado por GleisonJSilva
#Criado em : 01/10/2017, 17:37:20

import psycopg2
con = psycopg2.connect(host='localhost', port= 5432, 
database='dispositivo',
user='gleisongjs', password='jsilva996')
cur = con.cursor()
sql = 'create table mac (id serial primary key, mac varchar(20), nome varchar(50))'
cur.execute(sql)
macDispositivo = str(raw_input('digite o mac: '))
nomeDispositivo = str(raw_input('digite o nome: '))
sql = 'insert into mac(mac, nome) values(%s, %s)'
sqlDados = (macDispositivo, nomeDispositivo)
cur.execute(sql, sqlDados)
con.commit()
cur.execute('select * from mac')
recset = cur.fetchall()
for rec in recset:
    print (rec)
con.close()