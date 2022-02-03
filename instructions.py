from settings import Settings
from linked_list import LinkedList
from sorted_list import SortedList
from unsorted_list import UnsortedList
from disjoint_lists import DisjointLists

# this module execute the instructions from file or from typing.

instructions = {"MakeHeap": "make_heap",
                    "Insert": "insert",
                    "Minimum": "minimum",
                    "ExtractMin": "extract_min",
                    "Union": "union"}

# Flags to decide which list apply changes to.
first_heap, second_heap, union_heap = False, False, False
lst1, lst2, mergeable_heap = None, None, None


# get module (list type) and line to execute instruction.
def run_instruction(module, line):
    global first_heap, second_heap, union_heap
    global lst1, lst2, mergeable_heap

    # get the instruction from line
    inst = line.split()[0]

    # checks each instruction.
    if inst == "MakeHeap":
        if union_heap:
            lst1 = mergeable_heap
            lst2 = getattr(module, instructions[inst])(lst2)
            first_heap = False
            second_heap = True
            union_heap = False
        elif not first_heap:
            lst1 = getattr(module, instructions[inst])(lst1)
            first_heap = True
        else:
            lst2 = getattr(module, instructions[inst])(lst2)
            first_heap = False
            second_heap = True

    elif inst == "Insert":
        val = int(line.split()[1])  # convert string to int.
        if module.__name__ == 'DisjointLists':  # unique handling because of the unique parameters
            if union_heap:  # if insert to a mergeable heap
                getattr(UnsortedList, instructions[inst])(mergeable_heap, val)
            else:  # if insert to a any of the lists
                getattr(module, instructions[inst])(lst1, lst2, first_heap, val)
        else:
            if first_heap:
                getattr(module, instructions[inst])(lst1, val)
            elif second_heap:
                getattr(module, instructions[inst])(lst2, val)
            elif union_heap:
                getattr(module, instructions[inst])(mergeable_heap, val)

    elif inst == "Minimum":
        if first_heap:
            getattr(module, instructions[inst])(lst1)
        elif second_heap:
            getattr(module, instructions[inst])(lst2)
        elif union_heap:
            getattr(module, instructions[inst])(mergeable_heap)

    elif inst == "ExtractMin":
        if first_heap:
            getattr(module, instructions[inst])(lst1)
        elif second_heap:
            getattr(module, instructions[inst])(lst2)
        elif union_heap:
            getattr(module, instructions[inst])(mergeable_heap)

    elif inst == "Union":
        mergeable_heap = module()
        getattr(module, instructions[inst])(mergeable_heap, lst1, lst2)
        second_heap = False
        union_heap = True

    else:
        print('unknown instruction')

    Settings.print_inst_update(line, lst1, lst2, union_heap, mergeable_heap)


# get module (list type)
# wait for instruction from user
# execute instruction by calling run_instruction(module, line)
def read_manually(module):
    only_instructions = str(list(instructions.keys()))[1:-1] + ', \'Exit\'.\n'
    line = input(f'Choose 1 instruction: {only_instructions}')
    while line != 'Exit':
        run_instruction(module, line)
        line = input(f'Choose instruction: {only_instructions}\n')


# calls read_manually() or execute line by line
def read_instructions(input_):
    module = eval(input_.list_types[input_.list_type])

    if input_.input_types[input_.input_type] == 'Manually':
        read_manually(module)
    elif input_.input_types[input_.input_type] == 'File':
        for line in input_.lines:
            run_instruction(module, line)
