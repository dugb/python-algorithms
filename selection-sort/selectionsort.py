# selection sort
# find minimum item and move it to the beginning

a = [1000, 64, 25, 12, 22, 11, 65]
n = len(a)
b = []
i = 0
h = 0
print(a)


while n>0:
    h = 0 # this will be the index of our current minimum
    j=a[h] # j will be our minimum, number, we start with it set to arr[0]
    while (i < n):
        e = a[i]  
        if e > j:   # e is our current item
            j = j
            h = h   # index of current minimum is unchanged
        else:
            j = e
            h = i   # index of current minimum is updated
        i=i+1
    b.append(j)
    a.pop(h)
    i=0
    n = len(a)
    print(f"a = {a}")
    print(f"b = {b}")
    

