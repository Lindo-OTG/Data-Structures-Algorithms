from linked_list import LinkedList

def merge_sort(linked_list):
    '''
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list

    Runs in O(kn log n) time
    '''
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    '''
    Divide the unsorted linked list into sublists

    Takes O(k log n) time
    '''
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.node_at_index(mid-1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half
    
def merge(left, right):
    '''
    Merges Two linked lists, sorting by data in the nodes

    Returns a new, merged list

    Runs in O(n) time
    '''

    #C reate a new linked list that contains nodes from merging left and right
    merged = LinkedList()
    
    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right, until we reach the tail node of either
    while left_head or right_head:
        # If the head node of left is None, we're past the tail
        # Add the node from the right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set the loop condition to False
            right_head = right_head.next_node
        # If the head node of right is none, we're past the tail
        # Add the node from the left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set the loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain tail data tit perform comparison operation
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move the head to next node
                left_head = left_head.next_node
            # If data on left is greater than right, set current to right node
            else:
                current.next_node = right_head
                # Move the head to next node
                right_head = right_head.next_node
        
        # Move current to next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

#TODO: Write a rhobust verify function

# Test the code
linky = LinkedList()
linky.add(2)
linky.add(19)
linky.add(200)
linky.add(10)
linky.add(13)
linky.add(3)
linky.add(0)
linky.add(7)
linky.add(60)

print(f"Size: {linky.size()}")

print(linky)

print(f"Node and Index 3: {linky.node_at_index(3)}")

sorted_linky = merge_sort(linky)
print(sorted_linky)