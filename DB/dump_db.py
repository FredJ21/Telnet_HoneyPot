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
#print "\n-----------------------------------------------------------------------"

# -------------------------------------------------------------
req = "select date,ip,login,pass,timeout from telnet  ;"
cursor.execute(req) 

for (a) in cursor :

    if ( a[4] == 0):

        print str(a[0]) +" - 0000000000.00 - TCP 23 - Connexion from ip["+ a[1] +"] port[00000] login["+ a[2] +"] pass["+ a[3] +"]"

    else:

        print str(a[0]) +" - 0000000000.00 - TCP 23 - Connexion from ip["+ a[1] +"] port[00000] Timeout !!!"



cnx.close()


