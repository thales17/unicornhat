run:
	scp patterns.py pi@192.168.5.102:/home/pi/patterns.py
	ssh -t pi@192.168.5.102 "sudo python patterns.py"