class Node:
    '''
    An Object for storing a single node of a linked list.
    Models two arrtibutes - data and the link to the next node in the list.
    '''

    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data


    def __repr__(self) -> str:
        return f"<Node data: {self.data}>"


class LinkedList:
    '''
    Singly linked list
    '''

    def __init__(self) -> None:
        self.head = None


    def is_empty(self) -> bool:
        return self.head == None


    def size(self) -> int:
        '''
        Returns the number of nodes in the list.
        Takes O(n) time
        '''
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count


    def add(self, data) -> None:
        '''
        Adds a new Node containing data at the head of the list.
        Takes O(1) time.
        '''

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


    def search(self, key):
        '''
        Search for the first node containing data that matches the key.
        Returns the node or 'None' if not found.

        Takes O(n) time
        '''
        current = self.head
        while current:
            if current.data == key: return current
            else: current = current.next_node
        return None


    def insert(self, data, index):
        '''
        Inserts a new node Containing data at Index Positiion.
        Insertion takes O(1) time.
        But finding the node at the insertion point takes O(n) time.

        Takes overall O(n) time.        
        '''
        if index == 0: self.add(data)
        if index > 0: 
            new_node = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = Node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node
            prev_node.next_node = new_node
            new_node.next_node = next_node


    def remove(self, key):
        '''
        Removes Node containing data that matches the key.
        Returns the node or None if key doesn't exist.

        Takes O(n) time.
        '''
        current = self.head
        prev_node = None
        found = False

        while current and not found:
            if key == current.data and current is self.head:
                found = True
                self.head = current.next_node
            elif key == current.data:
                found = True
                prev_node.next_node = current.next_node
            else:
                prev_node = current
                current = current.next_node

        return current


    def remove_index(self, index):
        '''
        Removes Node containing data that matches the Index.
        Returns the removed node.

        Takes O(n) time.
        '''
        current = self.head

        nodes = []
        while current:
            nodes.append(current.data)
            current = current.next_node

        return self.remove(nodes[index])


    def node_at_index(self, index):
        '''
        Returns Node at the given Index.

        Takes O(n) time.
        '''
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position +=1

            return current


    def __repr__(self) -> str:
        '''
        Return a string representation of list.
        Takes O(n) time.
        '''
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node

        return '-> '.join(nodes)
