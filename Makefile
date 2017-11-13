run:
	scp patterns.py pi@192.168.5.200:/home/pi/patterns.py
	ssh -t pi@192.168.5.200 "sudo python patterns.py"