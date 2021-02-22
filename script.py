import platform
import os
import psutil
import subprocess

def disableall(p):
    addrs = psutil.net_if_addrs()
    f = open("interfaces.txt","w")
    print("\n")
    for i in addrs.keys():
        if p=="w":
            subprocess.call(['netsh', 'interface', 'set', 'interface', i, 'disabled'])
        elif p =="l":
            subprocess.call(['ifconfig', i, 'down'])
        print("Disabled:",i)
        f.write(i+"\n")
    f.close()
    print("\n")

def disableone(p):
    addrs = psutil.net_if_addrs()
    print("\nEnter an Interface Name to Disable:")
    for i in addrs.keys():
        print("  [-]"+i)
    choice = input("> ")
    try:
        if p=="w":
            subprocess.call(['netsh', 'interface', 'set', 'interface', choice, 'disabled'])
        elif p =="l":
            subprocess.call(['ifconfig', choice, 'down'])
        print("Disabled:",choice)
    except:
        print(choice,"is not a running Interface.")
    print("\n")
    
def enableall(p):
    f = open("interfaces.txt","r")
    interfaces = f.readlines()
    f.close()
    print("\n")
    for i in interfaces:
        i = i.strip()
        if p=="w":
            subprocess.call(['netsh', 'interface', 'set', 'interface',i, 'enabled'])
        elif p =="l":
            subprocess.call(['ifconfig', i, 'up'])
        print("Enabled:",i)
    print("\n")

def enableone(p):
    addrs = psutil.net_if_addrs()
    print("\nEnter an Interface Name to Enable:")
    choice = input("> ")
    try:
        if p=="w":
            subprocess.call(['netsh', 'interface', 'set', 'interface', choice, 'enabled'])
        elif p =="l":
            subprocess.call(['ifconfig', choice, 'up'])
        print("Enabled:",choice)
    except:
        print(choice,"is not a disabled Interface.")
    print("\n")

def interfaces():
    addrs = psutil.net_if_addrs()
    f = open("interfaces.txt","w")
    for i in addrs.keys():
        f.write(i+"\n")
    f.close()
        
def main():
    p = platform.system()
    print("[INTERFACE LOCKDOWN TOOL]\nOS:",p)
    print("="*24+"\n\n")

    if p=="Windows":
        p=("w")
    elif p=="Linux":
        p=("l")
    else:
        print("Unsupported OS, Exiting...")
        quit()
    interfaces()
    
    while (True):
        choice = input("Options:\n  [1]Disable All Interfaces\n  [2]Enable All Interfaces\n  [3]Disable Specific Interface\n  [4]Enable Specific Interface\n  [0]Quit\n> ")
        if choice=="1":
            disableall(p)
            continue
        elif choice=="2":
            enableall(p)
            continue
        elif choice=="3":
            disableone(p)
            continue
        elif choice=="4":
            enableone(p)
            continue
        elif choice=="0":
            print("Exiting...\n")
            quit()
        else:
            continue
        
main()
