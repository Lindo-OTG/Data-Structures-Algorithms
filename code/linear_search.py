def linear_search(list, target):
    '''
    Returns the index position of the target if found, else returns None.
    '''
    for i in range(0, len(list)):
        if list[i] == target : return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index index: ", index)
    else:
        print("Target not found")

numbers = [8,10,1,5,2,32,35,3,6,5,10,2,48,69,9,8,77,10]

result = linear_search(numbers, 3)
verify(result)

# val = linear_search([8,10,1,5,2,32,35,3,6,5,10,2,48,69,9,8,77,10], 3)
# print(val)
