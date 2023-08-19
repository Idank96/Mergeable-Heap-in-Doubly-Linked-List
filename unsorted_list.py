from linked_list import LinkedList, Node


class UnsortedList(LinkedList):
    """
    This class represents unsorted list.
    Using insert() of LinkedList class.
    Functions: makeheap, minimum, extract_min and union.
    """
    def __init__(self):
        super().__init__()

    def make_heap(self):
        """
        Make heap by calling the constructor
        Time complexity: O(1)
        """
        return UnsortedList()

    def minimum(self):
        """
        Search for the minimum value in the list
        Prints the minimum and return it.
        If list empty, do nothing.
        Time complexity: O(n)
        """
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

    def extract_min(self):
        """
        Search for the minimum value in the list
        Prints the minimum, remove and return it.
        If list is empty, do nothing.
        Time complexity: O(n)
        """
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

    def union(self, l1, l2):
        """
        Union 2 unsorted lists.
        Return the list itself if the 2nd is None.
        Set head of self as the head of the first list (l1)
        Set the next node of the tail of list 1 to head of list 2 (l2)
        Set the tail of self to list 2 tail.
        Time complexity: O(1)
        """
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
