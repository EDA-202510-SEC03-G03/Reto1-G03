def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function (element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def size (my_list): 
    return my_list["size"]

def add_first(my_list, element):
    insert_element(my_list, element, 0)
    return my_list


def first_element(my_list):
    element = my_list["elements"][0]
    return element

def add_last(my_list, element):
    insert_element(my_list, element, size(my_list))
    return my_list

def is_empty(my_list):
    empty = my_list["size"] == 0
    return empty

def last_element(my_list):
    last = my_list["elements"][(size(my_list)-1)]
    return last
     
def delete_element(my_list, index):
    if index < 0 or index >= size(my_list) or is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    list_size = size(my_list)
    if index != list_size - 1:
        for i in range(index, list_size - 1):
            my_list["elements"][i] = my_list["elements"][i+1]
    
    #my_list["elements"][list_size-1] = None
    my_list["elements"].pop()
    my_list["size"] -=1
    return my_list 
    

def remove_first(my_list):
    first_element = my_list["elements"][0]
    delete_element(my_list, 0)
    return first_element
    
def remove_last(my_list):
    last_element = my_list["elements"][size(my_list)-1]
    delete_element(my_list, size(my_list)-1)
    return last_element


def insert_element(my_list, element, index):
   #my_list["element"].insert(element, index)
   if index < 0 or index > size(my_list):
       raise Exception('IndexError: list index out of range')
   
   list_size = size(my_list)
   if index == list_size or is_empty(my_list):
        #my_list["elements"][list_size] = element
        my_list["elements"].append(element)
   else:
        for i in range(0, list_size - index-1):
            my_list["elements"][index+i+1] = my_list["elements"][index+i]
        my_list["elements"].append(my_list["elements"][list_size-1])
        my_list["elements"][index] = element
   
   my_list["size"] +=1
   return my_list 

def change_info(my_list, index, new_info):
    my_list["elements"][index] = new_info
    return my_list
     

def exchange(my_list, index1, index2):
    elemento_1 = my_list['elements'][index1]
    elemento_2 = my_list['elements'][index2]
    my_list['elements'][index1] = elemento_2
    my_list['elements'][index2] = elemento_1
    return my_list
     

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    sublista = new_list()
    for i in range(0, num_elements):
        sublista["elements"].append(my_list["elements"][pos + i])
    
    sublista["size"] = num_elements
    return sublista
    
def default_function(elemen_1, element_2):
   if elemen_1 > element_2:
      return 1
   elif elemen_1 < element_2:
      return -1
   return 0