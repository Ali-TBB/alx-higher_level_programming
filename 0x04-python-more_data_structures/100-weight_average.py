#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list and len(my_list):
        result = 0
        for i in my_list:
            result += i[0] * i[1]
        dev = 0
        for j in my_list:
            dev += j[1]
        return (result / dev)
    return 0
