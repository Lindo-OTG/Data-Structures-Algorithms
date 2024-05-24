def split(list):
    '''
    Divide the unsorted list at midpoint into sublists.
    Returns two sublists - left and right.

    Takes overall O(k log n) time
    '''

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    '''
    Merges two lists (arrays), sorting them in the process
    Returns a new merge list

    Takes overall O(n) time
    '''

    merged_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i+=1
        else:
            merged_list.append(right[j])
            j+=1
    
    while i < len(left):
        merged_list.append(left[i])
        i+=1
    
    while j < len(right):
        merged_list.append(right[j])
        j+=1

    return merged_list


def merge_sort(list):
    '''
    Sorts a given list in ascending Order.
    Returns a new sorted list.

    Takes O(kn log n) time
    '''

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def verify_sorted(list):
    n = len(list)

    if n <= 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])


listy = [6,8,1,12,15,71,63,39,20,15,5,10,4,47,42,52,36,58,49,61]  
m_listy = merge_sort(listy)
print(verify_sorted(listy)) # Should return False
print(verify_sorted(m_listy)) #Should return True