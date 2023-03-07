array = [10, 0, 11, 87, 21, 2, 22]
print(array)

ls = len(array)

for n in range(ls):

    for j in range(0, ls-n-1):
    
        if array[j] > array[j + 1]:

            array[j], array[j + 1] = array[j + 1], array[j]
    
print(array)
