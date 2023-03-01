def quickSort(array):

    if len(array) <= 1:
        return array

    else:
        prim = array[0]
        previous = []
        after = []
        
        for x in array[1:]:
            if x <= prim:
                previous.append(x)
        
            else:
               after.append(x)

        return quickSort(previous) + [prim] + quickSort(after)





array = [10, 0, 11, 87, 21, 2, 22]

sortarray = quickSort(array)

print(sortarray)

