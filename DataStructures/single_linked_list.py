import DataStructures.List.list_node as l_node

def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist


def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node ["next"]
        searchpos += 1
    return node["info"]


def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function (element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
            
    if not is_in_array:
        count = -1
    return count

def add_last(my_list, data):
    """new_node = {
        "info": data,
        "next": None
    }"""
    new_node = l_node.new_single_node(data)
    
    if my_list["first"] is None:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node  
    
    my_list["size"] += 1
    return my_list
    
def size(my_list):
    size = my_list["size"]
    return size

def first_element(my_list):
    #first = my_list["first"]["info"]
    return get_node(my_list, 0)["info"]
    
def get_node(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    i = 0
    temp = my_list["first"]
    while i < pos:
        temp = temp["next"]
        i += 1
    return temp
    
def change_info(my_list, pos, new_info):
    nodo = get_node(my_list, pos)
    nodo["info"] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    nodo1 = get_node(my_list, pos_1)
    nodo2 = get_node(my_list, pos_2)
    nodo1["info"], nodo2["info"] = nodo2["info"], nodo1["info"]
    return my_list

def add_first(my_list, element):
    return insert_element(my_list, element, 0)

def is_empty(my_list):
    return my_list["size"] == 0

def last_element(my_list):
    return get_element(my_list, my_list["size"] - 1)

def remove_first(my_list):
    first_element = get_element(my_list, 0)
    delete_element(my_list, 0)
    return first_element

def remove_last(my_list):
    last_element = get_element(my_list, size(my_list)-1)
    delete_element(my_list, size(my_list)-1)
    return last_element

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    new_Node = l_node.new_single_node(element)
    if is_empty(my_list):
        my_list["first"] = new_Node
        my_list["last"] = new_Node
    else:
        if pos == 0:
            new_Node["next"] = my_list["first"]
            my_list["first"] = new_Node["next"]
        elif pos == size(my_list):
            my_list["last"]["next"] = new_Node
            my_list["last"] = new_Node
        else:
            temp = get_node(my_list, pos - 1)
            new_Node["next"] = temp
            temp["next"] = new_Node
    my_list["size"] += 1
    return my_list

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
    else:
        temp  = get_node(my_list, pos - 1)
        temp["next"] = temp["next"]["next"]
    my_list["size"] -= 1
    return my_list
        

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    sub_list = new_list()
    for i in range (0, num_elements):
        insert_element(sub_list, get_node(my_list, pos + i)["info"], size(sub_list))
    sub_list["size"] = num_elements
    return sub_list