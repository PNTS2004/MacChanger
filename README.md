# MacChanger2 

This is a simple little Python script to change your MAC address using `macchanger`. It'll ask you for the following two inputs:

* What MAC address you want to switch to
* Which interface you want to apply it on (like `eth0` or `wlan0`)

Once you enter both, it goes ahead and runs the command to apply the change. The script runs the same `macchanger` command twice because sometimes `macchanger` command doesn't work if run once. Though it happens rarely but in to avoid it, the command is run twice to make sure that the MacChanger2 is working efficiently.

### Requirements

* Linux (any Debian-based distro should work fine)
* `macchanger` installed (`sudo apt install macchanger`)
* Root/sudo access

Example usage looks like this:

```bash
$ sudo python3 change_mac.py
Enter the New MAC: 00:11:22:33:44:55
Enter interface: eth0
```
* Note:
This change is temporary. Your MAC will reset when you reboot. It's also possible your device might reject certain MACs depending on the chipset, so if you see errors, try a different one.
