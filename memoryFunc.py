#!/usr/bin/env python3

import os

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
    return meminfo

if __name__ == "__main__":
    print(getMem())
