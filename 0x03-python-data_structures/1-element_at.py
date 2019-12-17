#!/usr/bin/python3
def element_at(my_list, idx):
    return (my_list[idx], None)[(0 <= idx < len(my_list))]
