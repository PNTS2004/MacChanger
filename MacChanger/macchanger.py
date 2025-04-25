#!/usr/bin/env python

import subprocess
import optparse

parser= optparse.OptionParser()

parser.add_option('-i', '--interface', dest='interface', help='Interface to change its Mac Address')
parser.add_option('-m', '--mac', dest='new_mac', help='New Mac Address')

(options, arguments) = parser.parse_args()

interface=options.interface
new_mac=options.new_mac

print('changing mac address')
subprocess.call('ifconfig '+interface+' down', shell=True)
subprocess.call('ifconfig '+interface+' hw ether '+new_mac, shell=True)
subprocess.call('ifconfig '+interface+' up', shell=True)
