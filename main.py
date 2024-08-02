#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'bonAppetit' function below.

# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b


def bonAppetit(bill, k, b):
    # Write your code here
    share_item = 0
    for i in range(len(bill)):
        if i != k:
            share_item += bill[i]
    b_actual = share_item // 2
    if b_actual == b:
        print("Bon Appetit")
    else:
        charge = b - b_actual
        print(charge)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)


