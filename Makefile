deploy:
	rshell -p /dev/ttyUSB0 rsync . /pyboard
