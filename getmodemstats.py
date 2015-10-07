#!/usr/bin/python
import sys
import telnetlib
import argparse

parser = argparse.ArgumentParser(description="Gets TP-Link TD-8840 Modem stats")
parser.add_argument('--stat',help="Stat to retrieve")
parser.add_argument('host',help="modem IP address")
parser.add_argument('user',help="modem username")
parser.add_argument('pw',help="modem password")

args = parser.parse_args()
stat = args.stat
host = args.host
user = args.user
pw = args.pw

tn = telnetlib.Telnet(host)

tn.read_until("username:")
tn.write(user+"\n")
tn.read_until("password:")
tn.write(pw+"\n")
tn.write("\n")

tn.read_until("TP-LINK(conf)#")
tn.write("adsl show info\n")
output = tn.read_until("cmd:SUCC")
tn.write('\x1d')
if stat == None:
    print output
else:
    for item in output.split("\n"):
        if stat in item:
            line = item.split("=")
            print line[1]

