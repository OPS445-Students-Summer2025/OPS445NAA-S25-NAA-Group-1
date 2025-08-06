#!/usr/bin/env python3

import subprocess

def netinfo():
    #Check if ifconfig is installed
    try:
        output = subprocess.check_output(['ifconfig'], stderr=subprocess.STDOUT, text=True)
        #Check the output of ifconfig. Combining error output and success out,
        # and return as string instead of bytes
    except subprocess.CalledProcessError:
        print("Error: 'ifconfig' command not found. Please install net-tools package")
        return


    #Splitting the output of ls to get interface list
    interfaces = subprocess.getoutput("ls /sys/class/net").split()
    #Create empty network dictionary
    network = {} 

    for nic in interfaces:
        #Get MAC address using awk
        mac = subprocess.getoutput(f"ip link show {nic} | awk '/link\\/(ether|loopback)/ {{print $2}}'")
        
        #Get IPv4 address using grep
        ip_info = subprocess.getoutput(f"ip -4 addr show {nic} | grep -oE 'inet ([0-9.]+/[0-9]+) brd ([0-9.]+)'")
        if nic == 'lo':
            #Handling loopback interface
            ipv4 = '00:00:00:00:00:00'
            broadcast = '00:00:00:00:00:00'
        else:
            #Split ip_info into strings and assign the ip address and broadcast address the correct index 
            ipv4 = ip_info.split()[1] 
            broadcast = ip_info.split()[3] 
                
        print(f'\n Interface: {nic}. \n IPv4: {ipv4}, \n Broadcast Address: {broadcast}, \n MAC address: {mac}')
        print('-' *40)




if __name__ == "__main__":
    netinfo()