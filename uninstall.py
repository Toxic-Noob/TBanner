#Coded By Dark Slad3
#A Product Of ToxicNoob

import os
import sys
import time

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

print("\033[92m")
os.system("clear")
time.sleep(0.8)
os.system("figlet ToxicNoob")
print("\033[3;90m                     Security Is An Illusion \033[0;92m")
print("\n")
time.sleep(0.6)
psb("\n[!] Loading...")
time.sleep(0.8)
psb("\n[!] Please Wait.....")
time.sleep(1)

print("\033[92m")
os.system("clear")
os.system("figlet TUninstall")
print("          	A Product Of ToxicNoob \033[0;92m")
print("\n")
time.sleep(1)

print("\n[01] Uninstall Security Only.")
print("[02] Uninstall Banner Only.")
print("[03] Uninstall Both Security and Banner.\n")
time.sleep(0.6)

op = input("[*] Enter Your Choice:> 0")
print("\n")

if(op=="1"):
	psb("[*] Please Wait....")
	os.system("rm /data/data/com.termux/files/home/.bashrc")
	os.system("rm /data/data/com.termux/files/home/.hushlogin")
	os.system("rm /data/data/com.termux/files/home/.Sec.py")
	time.sleep(1)
	psb("\n[*] Successfully Uninstalled Security From Termux...")
	time.sleep(1)
	psb("\n[*] Please Restart Your Termux...\n")
	time.sleep(1)
	
elif(op=="2"):
	psb("[*] Please Wait....")
	os.system("rm /data/data/com.termux/files/home/.bashrc")
	os.system("rm /data/data/com.termux/files/home/.hushlogin")
	os.system("rm /data/data/com.termux/files/home/.banner.txt")
	time.sleep(1)
	psb("\n[*] Successfully Uninstalled Banner From Termux...")
	time.sleep(1)
	psb("\n[*] Please Restart Your Termux...\n")
	time.sleep(1)
	
elif(op=="3"):
	psb("[*] Please Wait....")
	os.system("rm /data/data/com.termux/files/home/.bashrc")
	os.system("rm /data/data/com.termux/files/home/.hushlogin")
	os.system("rm /data/data/com.termux/files/home/.Sec.py")
	os.system("rm /data/data/com.termux/files/home/.banner.txt")
	time.sleep(1)
	psb("\n[*] Successfully Uninstalled Security and Banner From Termux...")
	time.sleep(1)
	psb("\n[*] Please Restart Your Termux...\n")
	time.sleep(1)
	
else:
	psb("\n[!] Please Choose an Correct Option...")
	time.sleep(1)
	os.system("python uninstall.py")
