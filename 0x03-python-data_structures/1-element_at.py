#!/usr/bin/python3
def element_at(my_list, idx):
    i = len(my_list)
    if (idx < 0) or (i <= idx):
        return
    else:
        return my_list[idx]
