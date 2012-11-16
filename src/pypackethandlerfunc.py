# -*- coding: utf-8 -*-
"""
Created on Thursday Nov 12 15:10:20 2012

@author: - Joshua White

"""

from scapy.all import *
import time
import multiprocessing

''' Constants for testing purposes '''
ip4_version = "4" 
ip4_ihl = "None"
ip4_tos = "0x1"
ip4_tot_len = "None"
ip4_id = '30'
ip4_frag_off = "0"
ip4_flg = "DF"
ip4_ttl = "32"
ip4_protocol = "ip" 
ip4_check = "0x0"
ip4_saddr = "172.16.1.1"
ip4_daddr = "1.1.1.1"

###################################################
### This defines the actual scripting interface ###

def eth_keys():
    
    return eth

def ip4_keys():
    ipv4 = IP(version=ip4_version, 
    ihl=ip4_ihl, 
    tos=ip4_tos,  
    len=ip4_tot_len,  
    id=ip4_id,  
    frag=ip4_frag_off, 
    flags=ip4_flg, 
    ttl=ip4_ttl,  
    proto=ip4_protocol, 
    chksum=ip4_check, 
    src=ip4_saddr,
    dst=ip4_daddr)

    return ipv4

def ip6_keys():
    
    return ip6
    
def tcp_keys():
    
    return tcp

def udp_keys():
    
    return udp
    
def isl_keys():
    
    return isl

def e1Q_keys():
    
    return e1Q
    
def arp_keys():
    
    return arp

def llc_keys():
    
    return llc

def lsn_keys():
    
    return lsn

def icm_keys():
    
    return icm
    
def cdp_keys():
    
    return cdp
    
def dtp_keys():
    
    return dtp
    
def bpd_keys():
    
    return bpd
    
def vSA_keys():
    
    return vSA
    
def vSU_keys():
    
    return vSU
    
def vAR_keys():
    
    return vAR

def vtJ_keys():
    
    return vtJ
    
def dhc_keys():
    
    return dhc

def hsr_keys():
    
    return hsr


''' More Testing '''

ipv4 = ip4_keys()

ipv4.show()