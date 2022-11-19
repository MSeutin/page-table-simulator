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

# get user input until EOF or Control D is presssed on MAC
# while True:
#     user_input = sys.stdin.read()
#     print(user_input)
    
while True:
    num = input()
    try:
        # if number is hex, change it to decimal
        if(num[:2] == '0x'):
            num = int(num, 16)
        # if number is decimal, change the string to an int
        else:
            num = int(num)
        # logic
        print(num)
    except:
        print("invalid entry")
        raise SystemExit

# close file
f.close()