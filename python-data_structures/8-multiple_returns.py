#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    else:
        f = sentence[:1]
        return int(len(sentence)), f
