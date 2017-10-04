#!/usr/bin/python
#-*-coding: utf-8 -*-
#Criado por GleisonJSilva
#Criado em : 01/10/2017, 17:37:20

import psycopg2
import sys

con = psycopg2.connect(host='localhost', database='dispositivo',
user = 'gleisongjs', password = 'jsilva996')



print 'OPÇÕES:'
print ''
print '1 - ADICIONAR'
print '2 - EDITAR'
print '3 - EXCLUIR'
print '4 - LISTAR'
print '5 - SAIR'
print '\n'

#Adicionando dados na tabela mac
def adicionar():
  
    cur = con.cursor()
    macDispositivo = str(raw_input('digite o mac: '))
    nomeDispositivo = str(raw_input('digite o nome: '))
    sql = 'insert into mac(mac, nome) values(%s, %s)'
    sqlDados = (macDispositivo, nomeDispositivo)
    cur.execute(sql, sqlDados)
    con.commit()
    print 'Dispositivo adicionado com sucesso\n'
    opcao()
    
    
#Editando dados na tabela mac
def editar():
    cur = con.cursor()
    sql = 'select * from mac'
    cur.execute(sql)
    tabela = cur.fetchall()
    for tab in tabela:
        print(tab)
    print '\n'
    
    #recebendo os dados que se deseja alterar
    idMac = int(raw_input('Digite o ID: '))
    macNovo = str(raw_input('Digite o mac: '))
    nomeNovo = str(raw_input('Digite o nome: '))
    
    #alterando os dados
    sql = """update mac
    set mac = %s, nome = %s
    where id = %s"""
    dados = (macNovo, nomeNovo, idMac)
    cur.execute(sql, dados)
    con.commit()
    print 'Dados alterados com sucesso\n'
    opcao()
 
    
#Excluindo dados na tabela mac
def excluir():
    cur = con.cursor()
    sql = 'select * from mac'
    cur.execute(sql)
    tabela = cur.fetchall()
    for tab in tabela:
        print (tab)
    print '\n'
    
    #excluindo os dados
    
    deleta = str(raw_input('Digite o ID que deseja deletar: '))
    sql = """delete from mac where id = %s"""
    cur.execute(sql, deleta)
    con.commit()
    print 'Dados deletados com sucesso\n'
    opcao()
    

#listando os dados da tabela mac    
def listar():
    cur = con.cursor()
    sql = 'select * from mac'
    cur.execute(sql)
    tabela = cur.fetchall()
    for tab in tabela:
        print (tab)
    opcao()
        
def opcao():
     
    op = int(raw_input('Digite a opção desejada: '))
    
    if op == 1:
        adicionar()
    elif op == 2:
        editar()
    elif op == 3:
        excluir()
    elif op == 4:
        listar()
    elif op == 5:
        con.close()
        sys.exit(0)
        
opcao()