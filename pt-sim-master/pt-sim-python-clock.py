#!/usr/bin/python3

import sys
import math
from sys import argv, stdin

# compute physical address
def addr(s, index, add):
    # using bitwise operators and or statement to get address
    return s["pages"][index]["frame"] << s["offset"] | (add & 2 ** s["offset"] - 1)

def read_table(file):
    with open(file, 'r') as f:
        line_one = f.readline().split()
        
        # michael & anudari 
        pt_dictionary = {
            "page_size": int(line_one[2]),
        }
        
        # list comprehension to make a 2d array of pt
        temp = [line.split() for line in f]
        
        # turn the above 2d array into dictionary (comprehension)
        d = ["valid_bit", "permission_bit", "frame", "recently_used"]
        pages = []
        
        # loop through pages
        for item in temp:
            item = [int(x) for x in item]
            pages.append(dict(zip(d, item)))
        
        pt = [x for x in pages if x != {}]
        pt_dictionary["pages"] = pt
        
    pt_dictionary["offset"] = int(math.log2(pt_dictionary["page_size"]))
    return pt_dictionary

def second_chance(state, clock, ind):
    while not state["pages"][ind]["valid_bit"]:
        current_idx = clock["pt_idxs"][clock["hand"]]
        current_frame = state["pages"][current_idx]["frame"]

        # reverse recently used bit
        if state["pages"][current_idx]["recently_used"]:
            state["pages"][current_idx]["recently_used"] = 0

        else:
            # evict page at present index
            state["pages"][current_idx]["valid_bit"] = 0
            state["pages"][current_idx]["frame"] = state["pages"][ind]["frame"]

            # swap evicted page with disk_page
            state["pages"][ind]["valid_bit"] = 1
            state["pages"][ind]["frame"] = current_frame

            # update page in clock
            clock["pt_idxs"][clock["hand"]] = ind

        # move clock hand
        l = len(clock["pt_idxs"])
        clock["hand"] = (clock["hand"] + 1) % l


def clock(pt_state):
    clock = {"pt_idxs": [i for i, page in enumerate(
        pt_state["pages"]) if page["valid_bit"]], "hand": 0}

    while virtual_address := stdin.readline():
        try:
            virtual_address = int(virtual_address)
        except ValueError:
            virtual_address = int(virtual_address, 16)

        # using bitwise operator for page location
        page_idx = virtual_address >> pt_state["offset"]

        if pt_state["pages"][page_idx]["valid_bit"]:
            pt_state["pages"][page_idx]["recently_used"] = 1
            print(hex(addr(pt_state, page_idx, virtual_address)))
        # check for permissions
        elif pt_state["pages"][page_idx]["permission_bit"]:

            # evict if necessary
            second_chance(pt_state, clock, page_idx)

            pt_state["pages"][page_idx]["recently_used"] = 1
            print("PAGEFAULT", hex(addr(
                pt_state, page_idx, virtual_address)))
        else:
            print("SEGFAULT")

clock(read_table(sys.argv[1]))
