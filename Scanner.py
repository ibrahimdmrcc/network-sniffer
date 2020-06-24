import nmap,netifaces
from mac_vendor_lookup import MacLookup



def GetGateWay():
    gateways = netifaces.gateways()
    gateway_listesi = gateways['default'][netifaces.AF_INET]

    return  gateway_listesi[0]

def NetworkTara(ip_araligi):

    cevaplar = []
    modemmac = ""

    nm = nmap.PortScanner()

    print("Ag Taraniyor... Lutfen Bekleyiniz...")
    a = nm.scan(ip_araligi, arguments='-sn')

    for k, v in a['scan'].items():
            if str(v['status']['state']) == 'up':
                try:
                    cevaplar.append([str(v['addresses']['ipv4']), str(v['addresses']['mac'])])
                except:
                    pass

    if len(cevaplar) == 0:
        print("Host bulunamadi!")

    else:
        print("\n * * * * * * Blunan Hostlar * * * * * * ")
        for i in range(len(cevaplar)):

            if(cevaplar[i][0] == GetGateWay()):
                modemmac = cevaplar[i][1]

            print("[",i,"]"," - Ip :",cevaplar[i][0],"- Mac :",cevaplar[i][1],"- Uretici Firma :",MacLookup().lookup(cevaplar[i][1]))

        hedef = int(input("Hedefin numarasi : "))

        #giden bilgilerin formatı = [hedef_ip,hedef_mac,modemin_ip,modemin_mac]
        giden_bilgiler = [cevaplar[hedef][0],cevaplar[hedef][1],GetGateWay(),modemmac]
        return giden_bilgiler