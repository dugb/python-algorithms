# binary search
# with an ordered list
# usage:    python3 bs.py numberToSearchFor
# example:  python3 bs.py 301

import math
import sys

a = [1, 3, 5, 6, 7, 8, 9, 21, 30, 32, 42, 47, 49, 53, 99, 101, 108, 300, 799, 758, 759, 800, 801, 500]
b = int(sys.argv[1])
print(f"looking for {b}")

# helper function to find the index of the middle element of an array.
def middle(x):
    return math.ceil((len(x)-1)/2)

# helper function to cut a list from an index up
def cutHalfUp(list, p):
    return list[p:]

# helper function to cut a list from an index down
def cutHalfDn(list, p):
    return list[:p]

check = None # the index of the item of the list we are checking against
print(a)  # our original list

while True:
    check = middle(a) # the index of the middle of a list
    print(a[check])
    if b == a[check]:  # if our item is in the list
        print('found')
        break
    elif b < a[check]:
        a = cutHalfDn(a,check)
    else:
        a = cutHalfUp(a,check)

    print(a) # the new list we will check against

    if len(a) == 1:  # got to the last item of the list without a match
        print("not found")
        break