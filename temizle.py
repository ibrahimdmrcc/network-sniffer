import os

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

Temizle()
