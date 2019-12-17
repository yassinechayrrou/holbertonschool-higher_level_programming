#!/usr/bin/python3
def element_at(my_list, idx):
    return (None, my_list[idx])[(0 <= idx < len(my_list))]
