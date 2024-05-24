def quicksort(values):
    if len(values) < 1:
        return values
    
    pivot = values[0]
    less_than_pivot = []
    greater_than_pivot = []

    for value in values[1:]:
        if value < pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
            # print("%15s, %1s, %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)



numbers = [6,8,1,12,15,71,63,39,20,15,5,10,4,47,42,52,36,58,49,61]    
sorted_numbers = quicksort(numbers)

print(sorted_numbers)