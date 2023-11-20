"Search for an element in tuple"

def search_element_tuple(element, my_tuple):
    if element in my_tuple:
        return True
    else:
        return False

def search_tuple(my_tuple, element): 
    try: 
        index = my_tuple.index(element)
        return f'the element {element} is found at index {index}'
    except ValueError:
        return f'the element {element} is not found in the tuple'
    
my_tuple = (1, 2, 3, 4, 5)
element = 3
print(search_tuple(my_tuple, element))

def searchTuple(my_tuple2, element2): 
    for i in range(0, len(my_tuple2)):
        if my_tuple2[i] == element2:
            return f'the element {element2} is found at index {i}'
    return f'the element {element2} is not found in the tuple'

# Example usage
my_tuple2=('a', 'b', 'c', 'd', 'e')
element2='e'
print(searchTuple(my_tuple2, element2))


# if search_tuple(my_tuple, element):
#     print("Element found in tuple")
# else:
#     print("Element not found in tuple")

# time complexity: O(n) - search through elements one by one
# space complexity: O(1) - no extra space used