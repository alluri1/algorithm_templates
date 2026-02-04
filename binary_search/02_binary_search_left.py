# type 02 - find the first value at which condition is met
# we are trying to move mid down until condition is met
# move one pointer when the condition is met, leave the other one at mid

# Guarantees Search Space is at least 2 in size at each step
#  Loop/Recursion ends when you have 1 element left.
# Post-processing required. Loop/Recursion ends when you have 1 element left.
# Need to assess if the remaining element meets the condition.

# example: first bad version, koko eating bananas, random pick with weight, find peak element,
# minimum in rotated sorted array
import math

def can_eat(piles, speed, h):
    hours = 0
    for pile in piles:
        if pile <= speed:
            hours += 1
        else:
            hours += math.ceil(pile/speed)
    return hours <= h

def binary_search(arr, h):
    l = 0
    r = len(arr) - 1
    # no equal sign
    while l < r:
        mid = (l+r)//2
        if not can_eat(arr, mid, h):
            l = mid +1
        else:
            # don't skip mid
            r = mid

    # End Condition: left == right
    return l
