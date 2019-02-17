# linear search
# good for short lists, because it’s simple and requires minimal code to implement.
# increment through a list checking each item

import sys

a=[81,34,10,2,11,71,13,8,99,34,12,1001,9,67]
f = int(sys.argv[1])

def search(f, a):
    for e in a:
        if f == e:
            print("found")
            return
    print("not found")
    return

search(f, a)