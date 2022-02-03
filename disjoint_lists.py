from unsorted_list import UnsortedList


# this class represents disjoint unsorted list.
# using insert(), minimum(), extract_min() and union() from UnsortedList class.
# functions: insert
class DisjointLists(UnsortedList):
    def __init__(self):
        super().__init__()

    # make heap by calling the constructor
    # time complexity: O(1)
    def make_heap(self):
        return DisjointLists()

    # if inserting to lst1 - no problem
    # if inserting to lst2 - check if the value not exists in lst 1, then insert.
    @staticmethod
    def insert(l1, l2, first_heap, value):
        if first_heap:
            super(DisjointLists, l1).insert(value)
        else:
            if super(DisjointLists, l2).value_in_dict(l1.dict, value):
                print(f'{value} exists in first heap')
            else:
                super(DisjointLists, l2).insert(value)
