#!/usr/bin/python
#-*-coding: utf-8 -*-
#Criado por GleisonJSilva
#Criado em : 01/10/2017, 18:18:42

import psycopg2
import nmap
import twitter


#Cria conexao com o db 
con = psycopg2.connect(host='localhost', database='dispositivo',
user='gleisongjs', password='jsilva996')
cur = con.cursor()
#extrai a tupla de mac e nome do db e converte em dicionário
cur.execute('select mac, nome from mac')
macs = dict(cur.fetchall())
con.close()

dispositivosConhecidos = []
dispositivosDesconhecidos = []

#Autenticação do twitter
api = twitter.Api(consumer_key='ftH2lqxvH6eTdYlQi78wbusnp', 
consumer_secret='oLgaI8Ia9HwZ2gPjQItTNIRiQiHkgRsvs4IxNl3gUX00EJ2Kzp',
access_token_key='832896102366068736-YtZwU7fMsHLuWYPhZLktZug8oTx7ua6',
access_token_secret='wSNwxnqIeJYoyQZAATOPruT6NcoGizJY8ENrk7JUZ9qId')

#Buscando os dispositivos conectados da minha rede
nm = nmap.PortScanner()
cidr2='192.168.0.1-254'

# rede da facul
#cidr2='10.1.4.0-254'

a=nm.scan(hosts=cidr2, arguments='-sP')

for k,v in a['scan'].iteritems():
    try:
        endMac = str(v['addresses']['mac'])
        if macs.has_key(endMac):
            dispositivo = macs[endMac]
            #lista de dispositivos conectados constantemente
            if dispositivo != 'TV' and dispositivo != 'roteador' and dispositivo != 'Ipad' and dispositivo != 'My PS4': #tratando os dispositivos fixos, televisão, roteador
                dispositivosConhecidos.append(dispositivo)
                aux = 1
                #print dispositivo 
            
        elif endMac != macs:
            dispositivo = endMac
            dispositivosDesconhecidos.append(dispositivo)
            #print desconhecido
            aux = 2
           
    except: print 'Este dispositivo' 

#jeito eficiente de concatenar string
dispositivosConhecidos = ', '.join(dispositivosConhecidos)
dispositivosDesconhecidos = ', '.join(dispositivosDesconhecidos)
#print dispositivosConhecidos
#print dispositivosDesconhecidos

#Twitando 
if aux == 1:
    status = api.PostUpdate('''@GleisonJSilva olhe quem está em casa agora: '''+dispositivosConhecidos)
    print status.text
elif aux==2:
    status = api.PostUpdate('@GleisonJSilva não conhecemos o dispositivo: '+ dispositivosDesconhecidos +' - Ele está utilizando a rede agora.')
    print status.text

