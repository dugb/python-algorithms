# insertion sort

 # On each loop iteration, insertion sort removes one element from the array. 
 # It then finds the location where that element belongs within another sorted 
 # array and inserts it there.

a = [101, 8, 3, 5, 13, 3, 2, 4]
c = []
print(a)
c.append(a[0]) # go ahead and put the first item from a into c
i=1 # since we already put the first item from a in c we'll start with the second item in a
while i < len(a):
    j=0
    while j < len(c):
        if a[i] < c[j]:
            c.insert(j, a[i])
            print(c)
            break
        else:
            j = j + 1
    i = i + 1

    