# -*- coding: utf-8 -*-
"""
Created on Thursday Nov 12 15:10:20 2012

@author: - Joshua White

"""
import datetime
import multiprocessing
import netifaces
import os
from pypackethandlerglobals import *


def GetDateTime():
    
    ''' This function gets the data and time for logging reasons '''

    InfoTimeNow = datetime.datetime.now().strftime('%m/%d/%G -- %T - <Info> -')
    WarningTimeNow = datetime.datetime.now().strftime('%m/%d/%G -- %T - <Warning> -')
    ErrorTimeNow = datetime.datetime.now().strftime('%m/%d/%G -- %T - <Error> -')

    return InfoTimeNow, WarningTimeNow, ErrorTimeNow

def ScriptUsage():

    ''' This function defines the help statements '''


    InfoTimeNow, WarningTimeNow, ErrorTimeNow = GetDateTime()
    NumCPUsAvailable = multiprocessing.cpu_count()    
    NetworkInterfacesAvailable = netifaces.interfaces()
    LinuxVersion = os.uname()
    
    print
    print InfoTimeNow, "This is PyPacketHandler Bench version:", VERSION
    print InfoTimeNow, "Number CPUs/Cores avalable:", NumCPUsAvailable
    print InfoTimeNow, "Network inerfaces available:", NetworkInterfacesAvailable  
    print InfoTimeNow, "Linux version:", LinuxVersion
   
    print ''' 
    
    Python Packet Handler Scripting Interface (PyPacketHandler): 
    
        - Is a system for simplifying the use of scapy to create/send custom packets in python

    Usage Options:

        - Do not specify more then one command line option at a time, we're not setup to handle that yet.

        -u / --unittests            :       Unittests for PyPacketHandler
        -s / --server               :       Run in Server (Listening) mode
        -c / --script [name]        :       Specify a script
        -f / --file   [name]        :       Specify data to be transported
        -c / --speed                :       Select the speed to send packets at
        -l / --logging              :       Enable logging
        -i / --interface [name]     :       Select an interface to transport on
        -v / --version              :       Get the current version information
 
    Example Usage:

        Server Mode:
            # python pypackethandler.py -s  

        Client Mode:
            # python pypackethandler.py -c scriptname.py -f filename.txt -c fast -i em1

    '''

ScriptUsage()