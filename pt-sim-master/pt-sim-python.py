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
SIZE = addr[2]

# log base 2 will give single page size
# Number of Bits used for Table Offset or Table Size
offset_bits = math.log(addr[2], 2)

# Number of rows in the page table
# Number of Bits used to Find any single Page in Table
page_bits = int(2**(addr[0] - offset_bits))

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
            print(f"hex to int: {num}")
        # if number is decimal, change the string to an int
        else:
            num = int(num)
            print(f"int to int: {num}")
        # LOGIC
        ## Turn the input into binary string
        num_bin = bin(num)
        num_bin = num_bin[2:]
        print(f"input number into bin without 0x: {num_bin}")
        
        ## pad binary with zeros on the left to make it the correct size
        
        ## Get the Page number bits reference to table in decimal
        
        
        ## Find Entry on Table, check if Valid bit is zero 
        
        
        ## If Entry bit is 1, proceed to find Frame number
        
        
        ## Add Frame number to Offset and create Physical Address
        
        
        ## Return Physical ADDRESS
    
    except:
        print("invalid entry")
        raise SystemExit
    
# End of stream!
print("done")

# close file
f.close()

# exit program
exit()