def binary_search(list, target):
    first = 0
    last = len(list)-1

    while first <= last:
        midpoint = (first + last)//2 #round down using the floor division operator

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    
    return None

def verify(index):
    if index is not None:
        print("Target found at index index: ", index)
    else:
        print("Target not found")

# numbers = [8,10,1,5,2,32,35,3,6,5,10,2,48,69,9,8,77,10]
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

result = binary_search(numbers, 3)
verify(result)
