#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    len = 0
    while(x >= len):
        try:
            print(my_list[x], end='')
            len += 1
        except:
            break
    return len
