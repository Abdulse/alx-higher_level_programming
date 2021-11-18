#!/usr/bin/python3
from hidden_4 import *

if __name__ == '__main__':
    for str in dir():
        if not (str[:2] != '__'):
            print(str)
