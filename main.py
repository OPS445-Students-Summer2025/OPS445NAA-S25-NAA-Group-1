#!/usr/bin/env python3

import subprocess
import sys


# Kerubel's Function - getMem()
'''
The getMem function will parse through the data in /proc/meminfo by opening and
displaying the first 3 lines of the file which contain general memory info into a dictionary
'''

def getMem():
    meminfo = {}
    f = open('/proc/meminfo', 'r')
    count = 0
    for line in f:
        count = count + 1
        if count > 3:
            break
        key = line.split(':')[0].strip() # Get description of numerical value
        value = line.split(':')[1].strip().split()[0] #Get numerical value only
        meminfo[key] = f'{round((int(value)/1024), 2)} mb' #convert kb to mb and round to nearest 10
    f.close()

    # I (FAISAL) HAVE MODIFIED IT SO THAT IT RETURNS INSTEAD OF PRINT SO THAT I CAN REUSE IT
    result = "" # for empty string
    for key in meminfo: #this will loop through each key in the meminfo dictionary
        result += f"{key}: {meminfo[key]}\n" #this will append the key-value pair to the result string
    return result


# Kyle's Function - netinfo()
def netinfo():
    #Check if ifconfig is installed
    try:
        output = subprocess.check_output(['ifconfig'], stderr=subprocess.STDOUT, text=True)
        #Check the output of ifconfig. Combining error output and success out,
        # and return as string instead of bytes
    except subprocess.CalledProcessError:
        return "Error: 'ifconfig' command not found. Please install net-tools package\n"
    
    #Splitting the output of ls to get interface list
    interfaces = subprocess.getoutput("ls /sys/class/net").split()
    #Create empty network dictionary
    network = ""
    
    for nic in interfaces:
         #Get MAC address using awk
        mac = subprocess.getoutput(f"ip link show {nic} | awk '/link\\/(ether|loopback)/ {{print $2}}'")

        #Get IPv4 address using grep
        ip_info = subprocess.getoutput(f"ip -4 addr show {nic} | grep -oE 'inet ([0-9.]+/[0-9]+) brd ([0-9.]+)'")
        if nic == 'lo':
            ipv4 = '00:00:00:00:00:00'
            broadcast = '00:00:00:00:00:00'
        else:
            #Split ip_info into strings and assign the ip address and broadcast address the correct index
            try:
                ipv4 = ip_info.split()[1] 
                broadcast = ip_info.split()[3] 
            except IndexError: #for cases where the networkr info is missing so that the code does not crash
                ipv4 = 'N/A'
                broadcast = 'N/A'
                
        network += f'\nInterface: {nic}\nIPv4: {ipv4}\nBroadcast Address: {broadcast}\nMAC address: {mac}\n' # we used the network += to return to the caller and build a full result string
        network += '-' * 40 + '\n'

    return network



# Edwin's part - Output Formatting
'''
This part of the code will do handling:
will be printing a line that tells the user what the program does
then it will handle the returned variables from functions
finally will display them
'''

def display_info(mem_data, net_data):
    print("==========================================================================================")
    print("Welcome! This program by group 1 displays system memory and network interface information.")
    print("==========================================================================================")
    print("\n>>> MEMORY INFO <<<")
    print(mem_data)
    print(">>> NETWORK INFO <<<")
    print(net_data)



# Faisal's Part - Save as a text file 
'''
My part will allow the user to choose whether to save memory or network info
to a file with a name they specify or both of them at the saem time
'''

def handle_options(mem_data, net_data):


    # This will retrieve commandline arguments excluding the script name
    args = sys.argv[1:]

    # This part will check if the user wants to save memory information
    if "savememory" in args:

        # Over here it will prompt the user to enter a filename for saving memory info
        filename = input("Enter the filename to save memory info (e.g., memory.txt): ")
        try:

            # Open the specified file in write mode
            f = open(filename, 'w')

            # Write the memory data to the file
            f.write(mem_data)

            f.close()

            print(f"Memory info saved to {filename}")
        except:

            # Handle any errors that occur during the file operation
            print("Error saving memory info")

    # Check if the user wants to save network information
    if "savenetwork" in args:

        # Prompt the user to enter a filename for saving network info
        filename = input("Enter filename to save network info (e.g., net.txt): ")
        try:
            # Open the specified file in write mode
            f = open(filename, 'w')

            # Write the network data to the file
            f.write(net_data)

            # Close the file
            f.close()

            # Inform the user that the network info has been saved
            print(f"Network info has been saved to {filename}")

        except:

            # Handle any errors that occur during the file operation
            print("Error saving network info")



# Main block
if __name__ == "__main__":
    # will call the functions to get data
    mem_data = getMem()
    net_data = netinfo()

    # will display info on screen
    display_info(mem_data, net_data)

    # Handle save options with the string datacollected from the functions
    handle_options(mem_data, net_data)
