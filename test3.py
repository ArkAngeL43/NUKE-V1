import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 
import datetime 
import os 
import sys 
import time 
from datetime import datetime

def GUI():
    date = str(datetime.now())
    root = Tk()

    #create image 
    image1 = Image.open("K.jpg")
    test = ImageTk.PhotoImage(image1)

    label1 = tkinter.Label(image=test)
    label1.image = test

    label1.place(x=25, y=25)

    #modify window
    root.title("Control Panel | By Scare Sec Hackers")
    root.geometry("250x170")
    root.configure(bg='black') 

    tab_control = ttk.Notebook(root)
    
    #Creating tabs
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    
    #Modifying tabs
    tab_control.add(tab1, text='Discover Network')
    tab_control.add(tab2, text='Scan Network')
############### DEFINITIONS #########################
    def start_tor():
        print("Tor Starting...")
        os.system(' sudo service tor start')
    
    def stop_tor():
        print("Tor Stoping......")
        os.system(' sudo service tor stop')

    def sys_after_stats_main_2():
        os.system('xterm -e sudo python3 sys-process.py --columns name,cpu_usage,memory_usage,status -n 20 --sort-by memory_usage --descending --live-update')
    
    def check_net():
        r = requests.get("https://google.com")
        print(" Checking Internet Connection..... ")
        t.sleep(1)
        print(" 200 = Good ")
        print("Response GIVEN => ", r.status_code)
    
    def scan_web():
        print(" ----------------------------- ")
        print(" EX - www.google.com")
        AWEB = str(input(" Enter A WWW link => "))
        print(" ----------------------------- ")
        s = socket.gethostbyname(f"{AWEB}")
        print("Your target => ", s)
        os.system(f' ruby scan.rb {AWEB} ')
    
########################### BUTTONS #####################
    #START TOR 
    btn = Button(root, text="Start Tor", bg="black", fg="white", command=start_tor())
    btn.grid(column=1, row=2, sticky='news')

    #STOP TOR
    btn = Button(root, text="Stop Tor", bg="black", fg="white", command=stop_tor())
    btn.grid(column=2, row=2, sticky='news')

    #SYSTEM STATS
    btn = Button(root, text="System Stats Live", bg="black", fg="white", command=sys_after_stats_main_2())
    btn.grid(column=2, row=2, sticky='news')
    #############FIND LOCATION FOR DEF############

    root.mainloop()

GUI()

