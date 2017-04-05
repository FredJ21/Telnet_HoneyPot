# Telnet HoneyPot

Telnet HoneyPot is a very simple listening process on the tcp port 23.

This Python script trap login and password, and disconnect the session 


## telnet_srv.py

  You can start the process easly :

	sudo ./telnet_srv.py
   or
	
	sudo ./telnet_srv.py > telnet_srv.log


## telnet_srv_log2db.py

  You can create database mysql with sql script :

	mysql -u root -p < DB/honey_DB.sql


  and, you can import datalog in database :

	./telnet_srv_log2db.py


## www/HoneyStat.html

  Simple statistics page 


## Example of my crontab :

	/etc/cron.d/telnet_srv_cron

	*/5 * * * *  root  /home/Telnet_HoneyPot/DB/telnet_srv_log2db.py >/dev/null 2>&1
	0,30 * * * *  root  /home/Telnet_HoneyPot/start.sh >/dev/null 2>&1

