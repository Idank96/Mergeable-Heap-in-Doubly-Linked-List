# this class represents the settings that the user choose.
# handles most of the input and output interactions
class Settings:
    list_types = {1: 'SortedList', 2: 'UnsortedList', 3: 'DisjointLists'}
    input_types = {1: 'File', 2: 'Manually'}

    list_type, input_type = None, None
    lines = []

    list_msg = "please enter the type of list you want:     \n" \
               f"1 - Sorted list                            \n" \
               f"2 - Unsorted list                          \n" \
               f"3 - Disjoint Unsorted list                 \n"

    input_msg = "please enter the type of input you want:       \n" \
                f"1 - {input_types[1]}                          \n" \
                f"2 - {input_types[2]}                          \n"

    def __init__(self):
        print("\nThis script implements a linked list with the following functions:     \n" 
              "Make-Heap, Insert, Minimum, Extract-Minimum and Union.              \n")
        self.list_type = int(input(self.list_msg))
        self.input_type = int(input(self.input_msg))
        self.lines = self.get_lines()

    def get_lines(self):
        if self.input_types[self.input_type] == "File":
            filename = input("insert filepath: ")
            print('----------------------')
            with open(filename, 'r') as f:
                return [line.strip() for line in f if line.strip()]

    def print_inst_update(self, lst1, lst2, union_heap, mergeable_heap):
        print(f'instruction: {self}\n')
        if union_heap:
            print('~~~ Mergeable Heap ~~~')
            mergeable_heap.print_list()
        elif lst1:
            print('~~~ HEAP 1 ~~~')
            lst1.print_list()
            if lst2:
                print('~~~ HEAP 2 ~~~')
                lst2.print_list()
        print('----------------------\n')
