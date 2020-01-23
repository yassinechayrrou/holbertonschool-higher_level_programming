#!/usr/bin/python3
class MyInt(int):
    """MyInt inherets from int with equal/different operators inverted"""
    def __eq__(self, value):
        return int.__ne__(self, value)

    def __ne__(self, value):
        return self - value == 0
