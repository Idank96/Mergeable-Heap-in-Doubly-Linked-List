from linked_list import LinkedList, Node


# this class represents unsorted list.
# using insert() of LinkedList class.
# functions: makeheap, minimum, extract_min and union.
class UnsortedList(LinkedList):
    def __init__(self):
        super().__init__()

    # make heap by calling the constructor
    # time complexity: O(1)
    def make_heap(self):
        return UnsortedList()

    # search for the minimum value in the list
    # prints the minimum and return it.
    # if list empty, do nothing.
    # time complexity: O(n)
    def minimum(self):
        if self.empty_list():
            return
        current = self.head
        minimum = Node(current.value)
        while current:
            if current.value < minimum.value:
                minimum = current
            current = current.get_next()

        print(f'The minimum is: {minimum.value}')
        return minimum

    # search for the minimum value in the list
    # prints the minimum, remove and return it.
    # if list is empty, do nothing.
    # time complexity: O(n)
    def extract_min(self):
        if self.empty_list():
            return

        # using minimum() function
        min = self.minimum()

        if min.value == self.head.value:
            self.head = self.head.get_next()
        elif min.value == self.tail.value:
            prev = min.get_prev()
            prev.set_next(None)
            self.tail = prev
        else:
            prev = min.get_prev()
            next = min.get_next()
            prev.set_next(next)
            next.set_prev(prev)

        self.heap_size -= 1
        self.dict.pop(min.value, None)
        print(f'Extract the minimum')
        return min

    # union 2 unsorted lists.
    # return the list itself if the 2nd is None.
    # set head of self as the head of the first list (l1)
    # set the next node of the tail of list 1 to head of list 2 (l2)
    # set the tail of self to list 2 tail.
    #  time complexity: O(1)
    def union(self, l1, l2):
        if (not l1 and not l2) or (not l1.head and (not l2 or not l2.head)):
            return
        elif l1.head and (not l2 or not l2.head):
            self.head = l1.head
            self.tail = l1.tail
            self.heap_size = l1.heap_size
            self.dict = l1.dict
        # if 2 lists exists:
        else:
            self.head = l1.head
            l1.tail.set_next(l2.head)
            l2.head.set_prev(l1.tail)
            self.tail = l2.tail
            self.dict = l1.dict | l2.dict   # only on python 3.9, merge dictionaries. It's instead of: self.dict = l1.update(l2)
            self.heap_size = len(self.dict)
