run:
	scp patterns.py pi@192.168.5.101:/home/pi/patterns.py
	ssh -t pi@192.168.5.101 "sudo python patterns.py"