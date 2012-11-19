# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:12:47 2012

@author: josh
"""

filename = "test.txt"
number_of_bytes = 8

with open(filename, 'rb') as f:
   while 1:
      byte_s = f.read(number_of_bytes)
      print byte_s
      if not byte_s:
         break
      byte = byte_s[0]