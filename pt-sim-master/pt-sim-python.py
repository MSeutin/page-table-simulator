#!/usr/bin/python3

import sys
import math

table_file = sys.argv[1]

# open Table file
f = open(table_file, 'r')

# splits the first line into 3 numbers -> N, M, & SIZE
addr = [int(n) for n in f.readline().split()]

# N is the number of bits in the virtual address
N = addr[0]

# M is the number of bits in the physical address
M = addr[1]

# SIZE is the size of a page in bytes
S = addr[2]

# Number of Bits used for Table Offset or Table Size
offset = int(math.log(S, 2))

# page number in page table 
num_pages = int(2**(N - offset))

# creates a 2D array of integers -> TABLE
pt = [list(map(int, line.split())) for line in f]

# Get rid of empty Array elements such as extra newlines at EOF
pt = [x for x in pt if x != []]

# get user input until EOF or Control D is presssed on MACc 
for line in sys.stdin:
    num = line.rstrip()
    try:
        # if number is hex, change it to decimal
        if(num[:2] == '0x'):
            num = int(num, 16)
        # if number is decimal, change the string to an int
        else:
            num = int(num)
        # LOGIC
        ## Turn the input into binary string
        num_bin = bin(num)
        num_bin = num_bin[2:]
        
        ## pad binary with zeros on the left to make it the correct size for logical address
        while(len(num_bin) < N):
            num_bin = '0' + num_bin
        
        ## separate actual_page_bits & actual_offset
        page_bits = N - offset
        actual_page_bits = num_bin[:page_bits]
        actual_offset = num_bin[page_bits:]
        
        ## computer actual_page_bits from binary to decimal to find entry in Table Index
        table_index = int(actual_page_bits, 2)
        
        ## Find Entry on Table, check if Valid bit is zero 
        table_row = pt[table_index]
        
        # If page not in physical mem but permission bit != 0, print DISK
        if table_row[0] == 0 and table_row[1] != 0:
            print('DISK')
        # If page not in physical mem and permission bit == 0, print SEGFAULT
        elif table_row[0] == 0 and table_row[1] == 0:
            print('SEGFAULT')
        else:
            frame_num = table_row[2]
            frame_bin = bin(frame_num)
            frame_bin = frame_bin[2:]
            physical_addr = frame_bin + actual_offset

            ## pad binary with zeros on the left to make it the correct size for logical address
            while(len(physical_addr) < M):
                physical_addr = '0' + physical_addr

            physical_addr = hex(int(physical_addr,2))
            print(physical_addr)
    
    except:
        print("invalid entry")
        raise SystemExit

# close file
f.close()

# exit program
exit()