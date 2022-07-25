#!/usr/bin/python3 
from scapy.all import * 
from prettytable import PrettyTable
from mac_vendor_lookup import MacLookup
from argparse import ArgumentParser
from sys import exit,stderr,argv


class NetworkScanner:
        def __init__(self,hosts):
                for host in hosts:
                        self.host = host
                        self.alive = {} 
                        self.create_packet()
                        self.send_packet()
                        self.get_alive()
                        self.print_alive()

        def create_packet(self):
                layer1 =  Ether(dst="ff:ff:ff:ff:ff:ff" )
                layer2 = ARP(pdst=self.host)
                packet = layer1 / layer2
                self.packet = packet 

        def send_packet(self):
                answered,unaswered = srp(self.packet,timeout=5,verbose=False)
                if answered:
                        self.answered = answered
                else:
                        print("No host is up")
                        sys.exit(1)

        def get_alive(self):
                for sent,recevied in self.answered:
                        self.alive[recevied.psrc] = recevied.hwsrc
        def print_alive(self):
                table = PrettyTable(["IP_Address","MAC_Address","Company_Name"])
                for ip,mac in self.alive.items():
                        try:
                                table.add_row([ip,mac,MacLookup().lookup(mac)])
                        except:
                                table.add_row([ip,mac,"unknown"])
                print(table)

def get_args():
        parser = ArgumentParser(description="NeTwOrK ScAnNeR")
        parser.add_argument("--s",dest="hosts",nargs="+",help="Hosts to Scan")
        arg=parser.parse_args()
        if len(sys.argv) ==1:
                parser.print_help(sys.stderr)
                sys.exit(1)
        return arg.hosts

hosts = get_args()
NetworkScanner(hosts) 
