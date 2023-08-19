from linked_list import LinkedList, Node


class SortedList(LinkedList):
    """
    This class represents sorted list.
    Functions: makeheap,insert, minimum, extract_min and union.
    """
    def __init__(self):
        super().__init__()


    @staticmethod
    def make_heap(self):
        """
        Make heap by calling the constructor
        Time complexity: O(1)
        """
        return SortedList()

    def insert(self, value):
        """
        Checks if value already in the list in O(1) with dictionary,
        else, insert it to the right position in the list and fix it.
        Time complexity: O(n)
        """
        if super(SortedList, self).value_in_dict(self.dict, value):
            return None
        node = Node(value)
        # if the head is null, insert value to head.
        if self.head is None:
            self.head = node
            self.tail = node
        # if the head should be at the end
        elif self.head.value >= node.value:
            node.set_next(self.head)
            self.head = node
        # find the node before the insertion node
        else:
            current = self.head
            while (current.get_next() is not None) and (current.get_next().value < node.value):
                current = current.get_next()
            node.set_next(current.get_next())
            current.set_next(node)
            if not node.get_next():
                self.tail = node

        self.heap_size += 1
        self.dict[value] = value

    def minimum(self):
        """
        Prints the minimum and return it.
        If list empty, do nothing.
        Time complexity: O(1)
        """
        if self.empty_list():
            return
        print(f'The minimum is: {self.head.value}')
        return self.head

    def extract_min(self):
        """
        # Prints the minimum, remove it from list, and dictionary return it.
        # If list empty, do nothing.
        # Time complexity: O(1)
        """
        if self.empty_list():
            return
        tmp_min = self.head.value
        self.head = self.head.get_next()
        self.heap_size -= 1
        self.dict.pop(tmp_min, None)
        print(f'Extract the minimum {tmp_min}')
        return tmp_min

    def union(self, l1, l2):
        """
        Union 2 sorted lists.
        Return the list itself if the 2nd is None.
        Starts from the the head of each list, find the minimum between the two,
        And get the next node after the minimum between the two.
        If any of the lists ends, it's filling the new list with the other one.
        Time complexity: O(n+k)
        """
        if (not l1 and not l2) or (not l1.head and (not l2 or not l2.head)):
            return
        elif l1.head and (not l2 or not l2.head):
            self.head = l1.head
            self.tail = l1.tail
            self.heap_size = l1.heap_size
            self.dict = l1.dict
        else:
            l1_current = l1.head
            l2_current = l2.head

            while l1_current and l2_current:
                if l1_current.value < l2_current.value:
                    l1_current = self.union_insert(l1_current)
                else:
                    l2_current = self.union_insert(l2_current)

            if l1_current:
                while l1_current:
                    l1_current = self.union_insert(l1_current)
            if l2_current:
                while l2_current:
                    l2_current = self.union_insert(l2_current)

    def union_insert(self, current):
        """
        Insert a node with the given value to the sorted list, 
        maintaining the sorted order.
        """
        super(SortedList, self).insert(current.value)   # insert to the end of list
        current = current.get_next()
        return current
