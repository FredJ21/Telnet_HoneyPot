#!/usr/bin/python
# coding: utf-8 

import sys
import re
import mysql.connector
from datetime import datetime

DB      = "honey"
DB_USER = "honey_user"
DB_PASS = "honey_pass"

colR = '\033[1;31m' # Red
colG = '\033[1;32m' # Green
colY = '\033[1;33m' # Yellow
colB = '\033[1;34m' # Blue
colW = '\033[1;37m' # Write 
colD = '\033[0;39m' # Default



# database connexion
cnx = mysql.connector.connect(host="localhost",user=DB_USER,password=DB_PASS, database=DB)
cursor = cnx.cursor()
print "\n-----------------------------------------------------------------------"

# -------------------------------------------------------------
req = "select count(*) from telnet"
cursor.execute(req) 
result = cursor.fetchone()
print "Nombre d'entrée dans la DB : "+ colG + str(result[0]) + colD


# -------------------------------------------------------------
req = "select count(*) from telnet where timeout = 0"
cursor.execute(req) 
result = cursor.fetchone()
print "Nombre de connection loin/pass : "+ colG + str(result[0]) + colD

# -------------------------------------------------------------
req = "select count(*) from telnet where timeout = 1"
cursor.execute(req) 
result = cursor.fetchone()
print "Nombre de connection en timeout : "+ colG + str(result[0]) + colD

# -------------------------------------------------------------
req = "select DATE_FORMAT(date,'%Y-%m-%d') as date2, count(*) from telnet group by date2 order by date2 desc limit 20;"
cursor.execute(req) 
print "Nombre de conection par JOUR :" 
for (a) in cursor :
    #print "\t"+ colB +  a[0].strftime('%Y-%m-%d') + colD + " --> ",  colG +  str(a[1]) + colD
    print "\t"+ colB +  str(a[0]) + colD + " --> ",  colG +  str(a[1]) + colD

# -------------------------------------------------------------
req = "select DATE_FORMAT(date,'%Y-%m-%d %H') as date2, count(*) from telnet group by date2 order by date2 desc limit 10 ;"
cursor.execute(req) 
print "Nombre de conection par HEURE :" 
for (a) in cursor :
    #print "\t"+ colB +  a[0].strftime('%Y-%m-%d %H:') + colD + " --> ",  colG +  str(a[1]) + colD
    print "\t"+ colB +  str(a[0]) + colD + " --> ",  colG +  str(a[1]) + colD

# -------------------------------------------------------------
req = "select login, count(*) as nb from telnet where timeout=0 group by login order by nb desc limit 10;"
cursor.execute(req) 
print "Login - TOP 10 :" 
for (a) in cursor :
    print "\t"+ colB +  a[0] + colD + " --> ",  colG +  str(a[1]) + colD

# -------------------------------------------------------------
req = "select pass, count(*) as nb from telnet where timeout=0 and pass<>'' group by pass order by nb desc limit 10;"
cursor.execute(req) 
print "Password - TOP 10 :" 
for (a) in cursor :
    print "\t"+ colB +  a[0] + colD + " --> ",  colG +  str(a[1]) + colD

# -------------------------------------------------------------

































print "-----------------------------------------------------------------------\n"



cnx.close()


