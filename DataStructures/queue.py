import DataStructures.List.single_linked_list as a

def new_queue():
    queue = a.new_list()
    return queue

def enqueue(my_queue: a, element):
    return a.add_last(my_queue, element)
    
def dequeue(my_queue: a):
    if is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty') 
    elemento_a_eliminar = a.first_element(my_queue)
    a.remove_first(my_queue)
    return elemento_a_eliminar


def peek(my_queue: a): 
    if is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty') 
    return a.get_element(my_queue, 0)
    
def is_empty(my_queue):
    return a.is_empty(my_queue)
       
def size(my_queue):
    return a.size(my_queue)