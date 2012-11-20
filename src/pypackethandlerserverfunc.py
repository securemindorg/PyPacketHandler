# -*- coding: utf-8 -*-

def RunServerMode():
    
    def eth_addr(a):

    ''' This function converts a 6 character ethernet address into 
        a dash seperated hex string to easier reading '''

    b = "%.2x-%.2x-%.2x-%.2x-%.2x-%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]),ord(a[4]) , ord(a[5]))
    return b

    # open a socket for raw mode listening, we use 0x003 for ETH_P_ALL which according
    # to the socket library documentation should collect every packet no matter the protocol
    s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
    
    # open a file to append the packets to for latter analysis
    filewrite = open("packet.cap", "a")
     	 
    # this loop gathers each packet that comes in within the 0 to 65565 port range
    # Then it write the packet and a new line character to the packet.cap, all in 
    # native Hex form
    while True:
        packet = s.recvfrom(65565)
        filewrite.write(str(packet))
        filewrite.write("\n")
    
        #get the packet string from the tuple
        packet = packet[0]
    
        ###############################################################
        ### This section parses out the ethernet header information ###
        eth_length = 14
    
        eth_header = packet[:eth_length]
        eth = unpack('!6s6sH' , eth_header)
        eth_protocol = socket.ntohs(eth[2])
    
        print 'Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' +eth_addr(packet[6:12]) +\
        ' Protocol : ' + str(eth_protocol)
    
        ################################################################
        ### This section parses out the IP packet header information ###
        if eth_protocol == 8 :
            #Parse IP header and take first 20 characters for the ip header
            ip_header = packet[eth_length:20+eth_length]
     	     
            #now unpack them
            iph = unpack('!BBHHHBBH4s4s' , ip_header)     
            version_ihl = iph[0]
            version = version_ihl >> 4
            ihl = version_ihl & 0xF
         
            iph_length = ihl * 4
         
            ttl = iph[5]
            protocol = iph[6]
            s_addr = socket.inet_ntoa(iph[8]);
            d_addr = socket.inet_ntoa(iph[9]);
    	     
            print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' +str(ttl) +\
            ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) +\
            ' Destination Address : ' + str(d_addr)
    
            ############################################################
            ### This section parses out TCP protocol header and data ###
            if protocol == 6 :
                t = iph_length + eth_length
                tcp_header = packet[t:t+20]
    
                #now unpack them :)
                tcph = unpack('!HHLLBBHHH' , tcp_header)
    
                source_port = tcph[0]
                dest_port = tcph[1]
                sequence = tcph[2]
                acknowledgement = tcph[3]
                doff_reserved = tcph[4]
                tcph_length = doff_reserved >> 4
    	       
                print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) +\
                ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) +\
                ' TCP header length : ' + str(tcph_length)
     	       
                h_size = eth_length + iph_length + tcph_length * 4
                data_size = len(packet) - h_size
     	       
                #get data from the packet
                data = packet[data_size:]
          
                print 'Data : ' + data
     	
         ######################################################     
     	#### This section parses out ICMP Packets and data ###
     	elif protocol == 1 :
                u = iph_length + eth_length
                icmph_length = 4
                icmp_header = packet[u:u+4]
     	 
                #now unpack them :)
     	    icmph = unpack('!BBH' , icmp_header)
     	     
                icmp_type = icmph[0]
     	    code = icmph[1]
     	    checksum = icmph[2]
     	    
     	    print 'Type : ' + str(icmp_type) + ' Code : ' + str(code) + ' Checksum : ' +str(checksum)
     	       
     	    h_size = eth_length + iph_length + icmph_length
     	    data_size = len(packet) - h_size
     	       
     	    #get data from the packet
     	    data = packet[data_size:]
     	       
     	    print 'Data : ' + data
     	     
         #######################################################
         ### This section parses out UDP packets and payload ###
     	elif protocol == 17 :
     	    u = iph_length + eth_length
     	    udph_length = 8
     	    udp_header = packet[u:u+8]
     	     
       	    #now unpack them
     	    udph = unpack('!HHHH' , udp_header)
     	       
     	    source_port = udph[0]
     	    dest_port = udph[1]
     	    length = udph[2]
     	    checksum = udph[3]
     	       
     	    print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) +\
                ' Length : ' + str(length) + ' Checksum : ' + str(checksum)
     	       
     	    h_size = eth_length + iph_length + udph_length
     	    data_size = len(packet) - h_size
     	       
     	    #get data from the packet
     	    data = packet[data_size:]
     	       
     	    print 'Data : ' + data
     	
         ############################################################################################
         ### This prints out a message that the packet was unknown and couldn't be decoded        ###
     	### In reality we could just build another parser but I don't feel like it at the moment ###
     	else :
     	    print "We couldn't decode the protocol, it was something other than TCP/UDP/ICMP"
     	    print