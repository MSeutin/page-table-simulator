#!/usr/bin/python3

import sys
import math

print("WELCOME TO MY PYTHON FILE")
table_file = sys.argv[1]
f = open(table_file, 'r')
addr = [int(n) for n in f.readline().split()]
print(type(addr[0]))
print(addr)

# log base 2 will give single page size
page_size = math.log(addr[2], 2) 

# number of rows in the page table
page_table_size = int(2**(addr[0] - page_size)) 

print(page_table_size)

# 2d array that holds the page table
page_table = [] 
for i in range(page_table_size):
    page_table.append(f.readline().split())

# make it int 2d table
page_table = [[int(num) for num in row] for row in page_table]

for row in page_table:
    print(row)
