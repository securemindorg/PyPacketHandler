# -*- coding: utf-8 -*-
"""
Created on Thursday Nov 12 15:10:20 2012

@author: - Joshua White

"""

from scapy.all import *
import time
import multiprocessing

''' Constants for testing purposes '''
'''
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
'''

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
    
    ipv6 = IPv6(version=ip6_version,
    to=ip6_tos,
    fl=ip6_flw,
    plen=ip6_plen,
    nh=ip6_nxt,
    hlim=ip6_hop,
    src=ip6_saddr,
    dst=ip6_daddr)    
    
    return ipv6
    
def tcp_keys():
    
    tcp = TCP(sport=tcp_source,
    dport=tcp_dest,
    seq=tcp_seq,
    ack=tcp_ack_seq,
    dataofs=tcp_doff,
    reserved=tcp_res1,
    flags=tcp_flg,
    window=tcp_window,
    chksum=tcp_check,
    urgptr=tcp_urp_ptr)    
    
    return tcp

def udp_keys():
    
    udp=UDP(sport=udp_source,
    dport=udp_dest,
    len=udp_len,
    chksum=udp_chk)    
    
    return udp
    
def isl_keys():
    
    return isl

def e1Q_keys():
    
    return e1Q
    
def arp_keys():
    
    return arp

def llc_keys():

    llc=LLC(dsap=llc_dsap,
    ssap=llc_ssap,
    ctrl=llc_control)
    
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
'''
ipv4 = ip4_keys()

ipv4.show()
'''