#!/usr/bin/env python3

import sys

# Save data as a text file
'''
My part will allow the user to choose whether to save memory or network info
to a file with a name they specify or both of them at the same time
'''

def handle_options(mem_data, net_data):


    # This will retrieve commandline arguments excluding the script name
    args = sys.argv[1:]

    # This part will check if the user wants to save memory information
    if "savememory" in args:

        # Over here it will prompt the user to enter a filename for saving memory info
        filename = input("Enter filename to save memory info (e.g., mem.txt): ")
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

            # will inform the user that the network info has been saved
            print(f"Network info saved to {filename}")

        except:

            # will handle any errors that will occur during the file operation
            print("Error saving network info")

if __name__ == "__main__":
    # I have added sample data here just to test my funuction works but in my final file it will use the dat from my groupmates memfunc and netfunc.
    mem_data = "MemTotal: 7852.0 mb\nMemFree: 1560.5 mb\nMemAvailable: 4312.0 mb\n"
    net_data = "Interface: eth0\nIPv4: 192.168.1.4\nBroadcast Address: 192.168.1.255\nMAC address: aa:bb:cc:dd:ee:ff\n"

    handle_options(mem_data, net_data)
