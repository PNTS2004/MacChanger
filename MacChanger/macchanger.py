#!/usr/bin/env python

import subprocess

interface=input('Interface: ')
new_mac=input('New Mac Address: ')
print('changing mac address')
subprocess.call('ifconfig '+interface+' down', shell=True)
subprocess.call('ifconfig '+interface+' hw ether '+new_mac, shell=True)
subprocess.call('ifconfig '+interface+' up', shell=True)