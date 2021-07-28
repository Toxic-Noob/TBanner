import os
import time
import sys

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


print("\033[34m")
os.system("clear")
os.system("figlet Security")
print("\n")
print("\033[92m")
time.sleep(1)

correctUsername = UniqU
correctPassword = UniqP


inuser = input("[*] Enter Username:> ")

if(inuser==correctUsername):
 inpass = input("[*] Enter Password:> ")
 if(inpass==correctPassword):
  psb("\n[!] Successfully Proved As "+correctUsername+" "+correctPassword+".....")
  time.sleep(0.6)
  psb("\n[!] Welcome!!!")
  time.sleep(0.9)
  os.system("clear")
 else:
  print("\n\033[31m[!] Wrong Password!!")
  time.sleep(0.8)
  os.system("python .Sec.py")
else:
 print("\n\033[31m[!] Wrong Username")
 time.sleep(0.8)
 os.system("python .Sec.py")
