#!/usr/bin/python3

import sys

print("WELCOME TO MY PYTHON FILE")
table_file = sys.argv[1]
f = open(table_file, 'r')
addr = [int(n) for n in f.readline().split()]
print(type(addr[0]))
print(addr)
