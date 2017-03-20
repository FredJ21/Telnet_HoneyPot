#!/usr/bin/python
# coding: utf-8 

import sys
import re
import mysql.connector
from datetime import datetime


FILE    = "telnet_srv.log"

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

# check nb of enter in table 
req = "select count(date) from telnet"
cursor.execute(req)

for (date) in cursor :
    nb_in_db = date[0]

# if table is empty
if nb_in_db > 0 : 
    # search last data insered
    req = "select date from telnet order by date desc limit 1"
    cursor.execute(req)

    for (date) in cursor :
        last_in_db = date[0]
else:
    last_in_db = datetime.strptime("2000-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')

print "Last data in DB : "+ str(last_in_db)



# ---------------------------------------------------------------------------------------------
count = 1
f = open(FILE, "r")
for line in f.readlines():

        line = line.rstrip('\n\r')
        line = line.replace(colR, '')
        line = line.replace(colG, '')
        line = line.replace(colY, '')
        line = line.replace(colB, '')
        line = line.replace(colW, '')
        line = line.replace(colD, '')

        m = re.search("(\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d) - \d+.\d+ - TCP 23 - Connexion from ip\[(\d+.\d+.\d+.\d+)\] port\[\d+\] (Timeout)", line)
        if not  m :
            m = re.search("(\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d) - \d+.\d+ - TCP 23 - Connexion from ip\[(\d+.\d+.\d+.\d+)\] port\[\d+\] login\[(.*)\] pass\[(.*)]", line)


        if m:
    
            date = m.group(1)
            ip   = m.group(2)
            date_objet = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

            if date_objet > last_in_db:

                if m.group(3) == "Timeout" :

                    req = "INSERT INTO telnet (date, ip, timeout) VALUES ('"+ date +"', '"+ ip +"', 1);"
                    print str(count), req
                    cursor.execute(req)
                    cnx.commit()

                else :

                    login = m.group(3)
                    passw = m.group(4)

                    req = "INSERT INTO telnet (date, ip, login, pass) VALUES ('"+ date +"', '"+ ip +"', '"+ login +"', '"+ passw +"')"
                    print str(count), req
                    cursor.execute(req)
                    cnx.commit()

                count = count + 1

        else :

            print colR +"ERROR: "+ colD, line 





f.close()
cnx.close()



