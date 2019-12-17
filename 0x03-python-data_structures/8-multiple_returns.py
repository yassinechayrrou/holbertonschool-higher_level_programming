#!/usr/bin/python3
def multiple_returns(sentence):
    tup = (len(sentence), sentence[0])
    if sentence:
        return tup
    else:
        tup = (len(sentence), None)
        return tup
