import psutil
from datetime import datetime
import pandas as pd
import time
import sys 
from sys import platform
import os

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
    """
    Returns size of bytes in a nice format
    """
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
        #restart_program() auto define live update 
