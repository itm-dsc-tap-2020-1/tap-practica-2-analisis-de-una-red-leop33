import os
hostname="www.itmorelia.edu.mx"
respuesta=os.system("ping -c 1 "+hostname)
if respuesta==0:
    print(hostname+": esta en funcionamiento")
else:
        print(hostname+" No funciona")
red="200.33.171.0/24"
os.system("nmap -sP " + red)
"""Starting Nmap 7.80 ( https://nmap.org ) at 2020-02-27 11:42 CST
Nmap scan report for mail.itmorelia.edu.mx (200.33.171.3)
Host is up (0.0040s latency).
Nmap scan report for 200.33.171.13
Host is up (0.0021s latency).
Nmap scan report for 200.33.171.63
Host is up (0.0072s latency).
Nmap scan report for denebvirtual.itmorelia.edu.mx (200.33.171.77)
Host is up (0.0058s latency).
Nmap scan report for sappp.itmorelia.edu.mx (200.33.171.80)
Host is up (0.0054s latency).
Nmap scan report for 200.33.171.85
Host is up (0.0049s latency).
Nmap scan report for 200.33.171.99
Host is up (0.033s latency).
Nmap scan report for 200.33.171.115
Host is up (0.0053s latency).
Nmap scan report for vinculacion.itmorelia.edu.mx (200.33.171.124)
Host is up (0.0030s latency).
Nmap scan report for 200.33.171.125
Host is up (0.021s latency).
Nmap done: 256 IP addresses (10 hosts up) scanned in 4.88 seconds"""