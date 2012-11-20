# -*- coding: utf-8 -*-
"""
Created on Thursday Nov 12 15:10:20 2012

@author: - Joshua White

"""

from pypackethandlerglobals import *
from pypackethandlerserverfunc import RunServerMode
from pypackethandlerpacketfunc import *
from pypackethandlerfunc import *
import sys
import getopt
import subprocess



def main(argv):

    ''' This is the main function '''
        
    try:
        opts, args = getopt.getopt(argv, "h?usc:f:s:li:v", ["help", "unittests", 
                                                          "server", "script=", 
                                                          "file=", "speed=", "logging",
                                                          "interface=", "version"])
    except getopt.GetoptError:
        sys.exit(2)
       
    if opts > 0:

        for option, argument in opts:
    
            if option in ("-h", "-?", "--help"): 
                ScriptUsage()              
                sys.exit()
                
            elif option in ("-u", "--unittests"):
                print "Unittests"
    
            elif option in ("-s", "--server"):
                RunServerMode()
            
            elif option in ("-c", "--script"):
                SCRIPTNAME = argument
                print SCRIPTNAME
            
            elif option in ("-f", "--file"):
                FILENAME = argument
                print FILENAME
                
            elif option == ("-d", "--speed"):
                SPEED = argument
                print SPEED
            
            elif option in ("-l", "--logging"):
                print "logging on"
                
            elif option == ("-i", "--interface"):
                INTERFACE = argument
                print INTERFACE
                 
            elif option in ("-v", "--version"):
                PrintVersion()
 
if __name__ == "__main__":
    main(sys.argv[1:])