def mergeSort(array):
    if len(array) > 1:
        
        midArray = len(array) // 2
        previous = array[:midArray]
        after = array[midArray:]

        # keeps separating the arrays
        mergeSort(previous)
        mergeSort(after)


        x = y = w = 0

        while x < len(previous) and y < len(after):
        
            if previous[x] < after[y]:
        
                array[w] = previous[x]
                x += 1
        
            else:
        
                array[w] = after[y]
                y += 1
        
            w += 1

        while x < len(previous):
        
            array[w] = previous[x]
            x += 1
            w += 1

        while y < len(after):
        
            array[w] = after[y]
            y += 1
            w += 1


array = [10, 0, 11, 87, 21, 2, 22]

mergeSort(array)
    
print(array)
