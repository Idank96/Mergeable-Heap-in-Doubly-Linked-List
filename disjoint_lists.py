from unsorted_list import UnsortedList


class DisjointLists(UnsortedList):
    """
    This class represents disjoint unsorted list.
    Using insert(), minimum(), extract_min() and union() from UnsortedList class.
    Functions: insert
    """
    def __init__(self):
        super().__init__()

    def make_heap(self):
        """
        Make heap by calling the constructor
        Time complexity: O(1)
        """
        return DisjointLists()

    @staticmethod
    def insert(l1, l2, first_heap, value):
        """
        If inserting to lst1 - no problem
        If inserting to lst2 - check if the value not exists in lst 1, then insert.
        """
        if first_heap:
            super(DisjointLists, l1).insert(value)
        else:
            if super(DisjointLists, l2).value_in_dict(l1.dict, value):
                print(f'{value} exists in first heap')
            else:
                super(DisjointLists, l2).insert(value)
