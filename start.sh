#!/bin/sh


PID=`ps aux | grep telnet_srv.py | grep -v grep | awk '{print $2}'`
CPU=`top -b -p $PID -n 1 | tail -1 | awk '{print $9*100}'`



if [ ! $CPU ]; then

	# restart if process is not present
	echo start telnet_srv
	/home/Telnet_HoneyPot/telnet_srv.py >> /home/Telnet_HoneyPot/telnet_srv.log&

elif [ $CPU -gt '9000' ]; then

	# kill & restart if cpu is exceeded
	echo kill and restart telnet_srv
	killall telnet_srv.py
	sleep 1
	/home/Telnet_HoneyPot/telnet_srv.py >> /home/Telnet_HoneyPot/telnet_srv.log&
fi

