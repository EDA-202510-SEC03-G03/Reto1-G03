import DataStructures.List.array_list as sl

def new_stack():
    return sl.new_list()

def push(my_stack, element):
    return sl.add_last(my_stack, element)

def pop(my_stack):
    if is_empty(my_stack):
        raise Exception('EmptyStructureError: stack is empty') 
    elemento_a_eliminar = top(my_stack)
    sl.delete_element(my_stack, size(my_stack)-1)
    return elemento_a_eliminar

def is_empty(my_stack):
    return sl.is_empty(my_stack)

def top(my_stack):
    if is_empty(my_stack):
        raise Exception('EmptyStructureError: stack is empty') 
    return sl.last_element(my_stack)

def size(my_stack):
    return sl.size(my_stack)