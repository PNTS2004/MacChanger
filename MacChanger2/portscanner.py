import subprocess

mac=input('Enter the New MAC: ')
interface=input('Enter interface: ')

subprocess.run(["macchanger", "-m", mac, interface])
subprocess.run(["macchanger", "-m", mac, interface])
