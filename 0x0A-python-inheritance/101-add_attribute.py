#!/usr/bin/python3
def add_attribute(obj, attribute, value):
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
