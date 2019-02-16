# bubble sort
# repeatedly swap adjacent elements if they are in wrong order.

a = [ 1001, 7, 0, 12, 10, 21, 5, 1, 4, 99, 1000, 3, 71, 2, 8]
n = len(a)
i=0
print(a)
swaps = 0 # swap counter
while True:
    b = a[i]
    c = a[i+1]
    if b > c: # a swap is needed
        a[i]=c
        a[i+1]=b
        swaps = swaps + 1 # a swap occured
    i=i+1
    # if we get to the end, then we start over, unless we are done
    if i == n-1:
        print(f"pass complete, {swaps} swaps")
        if swaps == 0: # no swaps occured, I think we are done
            break
        i=0
        swaps = 0 # reset swap counter
    print(a)