import socket
import sys
import os
ANY = '0.0.0.0'
SENDERPORT=1501
MCAST_ADDR = '224.168.2.9'
MCAST_PORT = 8946
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.bind((ANY,SENDERPORT))
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)

#User arguments
messageFile = open('msg.txt', 'r')
messageFileText = messageFile.read()
messageFile.close()
os.system("rm msg.txt")

sock.sendto(messageFileText, (MCAST_ADDR,MCAST_PORT) )
sock.close()