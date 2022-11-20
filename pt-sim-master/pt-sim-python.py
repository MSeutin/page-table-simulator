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
        print(f"TABLE ROW: {table_row}")
        
        ## If Entry bit is 1, proceed to find Frame number
        
        
        ## Add Frame number to Offset and create Physical Address
        
        
        ## Return Physical ADDRESS
        # code below converts a binary number into an hex
        # hex(int('1010),2) -> becomes 0xa
        
        
        # more useful code for later
        # n_int = 10 # 10
        # n_bin = bin(n_int) # '0b1010'
        # n_bin = '000' + n_bin[2:] # '0001010'
        # print(hex(int(n_bin, 2))) # prints 0xa
    
    except:
        print("invalid entry")
        raise SystemExit
    
# End of stream!
print("done")

# close file
f.close()

# exit program
exit()