#pip3 install psutil pandas
#sudo pip install pandas && pip install pandas && pip3 install pandas && pip3 install panda && pip install panda
import psutil 
from datetime import datetime
import pandas as pd 
import time 
import os 

def get_processor_info():
    processes = []
    for process in psutil.process_iter():
        with process.oneshot():
            pid = process.pid 
            if pid == 0:
                continue 
                name = process.name()
                try:
                    create_time = datetime.fromtimestamp(process.create_time())
                except PSError:
                    create_time = datetime.fromtimestamp(psutil.boot_time())
                    try:
                        cores = len(process.cpu_affinity())
                    except psutil.AccessDenied:
                        cores = 0
                    # get the CPU usage %
                    cpu_usage = process.cpu_percent()
                    status = process.status()
                    try:
                        nice = itn(process.nice())
                    except psutil.AccessDenied:
                        nice = 0 



# test def one by one 
if __name__ == "__main__":
    get_processor_info()