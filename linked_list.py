class LinkedList:
    """
    This class represents linked list.
    Functions: insert, print_list, empty_list, value in dict.
    """
    def __init__(self, head=None, tail=None):
        self.dict = {}
        self.head = head
        self.tail = tail
        self.heap_size = 0


    def insert(self, value):
        """
        Checks if value already in the list in O(1) with dictionary,
        Else, insert it to end of list.
        Time complexity: O(1)
        """
        if self.value_in_dict(self.dict, value):
            return None

        tmp = Node(value)
        if not self.head:
            self.head = tmp
            self.head.set_next(None)
            self.head.set_prev(None)
            self.tail = self.head
        else:
            tmp.set_next(None)
            tmp.set_prev(self.tail)
            self.tail.set_next(tmp)
            self.tail = tmp

        self.heap_size += 1
        self.dict[value] = value
        return tmp


    def print_list(self):
        """
        Prints current list, head, tail, heap_size and dictionary of self (list).
        Iterating over the list.
        Time complexity: O(n)
        """
        tmp_list = []
        current = self.head
        while current:
            tmp_list.append(current.value)
            current = current.get_next()
        print(f'current list: {tmp_list}')
        # uncomment to see full details:
        if self.head:
            print(f'head: {self.head.value}')
            print(f'tail: {self.tail.value}')
            print(f'heap_size: {self.heap_size}')
            print(f'dict: {self.dict}\n')

    
    def empty_list(self):
        """
        If list empty return true, else false.
        """
        if not self.head:
            print(f'List is empty')
            return True
        else:
            return False

    
    @staticmethod
    def value_in_dict(lst, value):
        """
        If value in dict return true, else return false.
        """
        return True if value in lst else False


class Node:
    """
    This class represents a node in a linked list.
    Functions: get_next, set_next, get_prev, set_prev.
    """
    def __init__(self, value=0, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def get_prev(self):
        return self.prev_node

    def set_prev(self, new_prev):
        self.prev_node = new_prev
