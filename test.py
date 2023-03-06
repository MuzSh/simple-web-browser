#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

if __name__ == '__main__':
    for e in range(1,15):
        print(fizzBuzz(e))
