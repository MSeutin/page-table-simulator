#!/usr/bin/python3

import sys

print("WELCOME TO MY PYTHON FILE")
table_file = sys.argv[1]
input_file = sys.argv[2]
t_file = open(table_file, 'r')
in_file = open (input_file, 'r')
print(t_file.read())
print()
print(in_file.read())
