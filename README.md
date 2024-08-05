# Black-ARP, ARP Spoofer Tool
=====================

A Python-based tool for performing ARP spoofing attacks on a local network.

## Description
---------------

This tool uses the Scapy library to send ARP packets to a target device and its gateway, effectively spoofing the MAC address of the gateway and allowing the attacker to intercept traffic between the target and the gateway.

## Usage
-----

1. Run the script using Python 3: `python3 black.py`
2. Select the network interface to use for the attack.
3. Enter the IP address of the target device.
4. Enter the IP address of the gateway (router).
5. The tool will start sending ARP packets to the target and gateway, spoofing the MAC address of the gateway.
