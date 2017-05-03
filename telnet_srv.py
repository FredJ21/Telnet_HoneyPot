#!/usr/bin/python
# coding: utf-8 

import socket
import threading
import sys
import time

PORT    = 23
TIMEOUT = 10

colR = '\033[1;31m' # Red
colG = '\033[1;32m' # Green
colY = '\033[1;33m' # Yellow
colB = '\033[1;34m' # Blue
colW = '\033[1;37m' # Write 
colD = '\033[0;39m' # Default



class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket, Nb):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        self.clientsocket.settimeout(TIMEOUT)
        self.Nb = Nb
        #print("[+] New thread for %s %s %d" % (self.ip, self.port, self.Nb))


    def run(self): 

        # test the first sent data 
        self.clientsocket.settimeout(1)
        try:
            r = self.clientsocket.recv(2048)
        except socket.timeout:
            pass

        self.clientsocket.settimeout(TIMEOUT)
        try:

            login = ""
            password = ""

            # ----------------------------------------------
            # login
            self.clientsocket.send("Login: ")
            a = 0
            while True:
                rep = self.clientsocket.recv(2048)
                login += rep
                if login[-1:] == '\n':
                    break
                if a > 200 :
                    break
                a += 1
                time.sleep(0.01)
                #self.clientsocket.send(str(a))
            login = login.rstrip('\n\r')


            # ----------------------------------------------
            # password
            self.clientsocket.send("Password: ")
            a = 0
            while True:
                rep = self.clientsocket.recv(2048)
                password += rep
                if password[-1:] == '\n':
                    break
                if a > 200 :
                    break
                a += 1
                time.sleep(0.01)
            password = password.rstrip('\n\r')



            # ----------------------------------------------
            # Output
            DATE = str(time.strftime('%Y-%m-%d %H:%M:%S')) +' - '+ str(time.time())
            print ("%s - TCP %s - Connexion from ip[%s%s%s] port[%s] login[%s%s%s] pass[%s%s%s]" % (DATE, PORT, colB, self.ip, colD, self.port, colG, login, colD, colR, password, colD))
            sys.stdout.flush()

            self.clientsocket.send("Login incorrect !\n")
            self.clientsocket.close()

        #except socket.timeout:
        except :
            DATE = str(time.strftime('%Y-%m-%d %H:%M:%S')) +' - '+ str(time.time())
            print ("%s - TCP %s - Connexion from ip[%s%s%s] port[%s] %sTimeout !!!%s" % (DATE, PORT, colB, self.ip, colD, self.port, colR, colD))
            sys.stdout.flush()
            self.clientsocket.close()

        #print("[+] End thread pour %s %s %d" % (self.ip, self.port, self.Nb))



# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
DATE = str(time.strftime('%Y%m%d-%H:%M:%S')) +' - '+ str(time.time())

print ("%s - Start server to TCP port %d" % (DATE, PORT))
sys.stdout.flush()

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",PORT))

Nb = 0;


while True:
    tcpsock.listen(10)
    (clientsocket, (ip, port)) = tcpsock.accept()


    newthread = ClientThread(ip, port, clientsocket, Nb)
    newthread.start()

    Nb += 1


print ("END")


