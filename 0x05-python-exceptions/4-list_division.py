#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    len = 0
    for i in range(list_length):
        try:
            result[i] = my_list_1[i] / my_list_2[i]
            len += 1
        except ZeroDivisionError:
            print("division by 0")
            break
        except TypeError:
            print("wrong type")
            break
        except IndexError:
            print("out of range")
            break
        finally:
            print(result)
    return len

