
# this class represents linked list.
# functions: insert, print_list, empty_list, value in dict.

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.dict = {}
        self.head = head
        self.tail = tail
        self.heap_size = 0

    # checks if value already in the list in O(1) with dictionary,
    # else, insert it to end of list.
    # time complexity: O(1)
    def insert(self, value):
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

    # prints current list, head, tail, heap_size and dictionary of self (list).
    # iterating over the list.
    # time complexity: O(n)
    def print_list(self):
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

    # if list empty return true, else false.
    def empty_list(self):
        if not self.head:
            print(f'List is empty')
            return True
        else:
            return False

    # if value in dict return true, else return false.
    @staticmethod
    def value_in_dict(lst, value):
        return True if value in lst else False


# this class represents a node in a linked list.
# functions: get_next, set_next, get_prev, set_prev.
class Node:
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
