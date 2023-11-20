# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(my_tuple[0])  # Output: 1

# Concatenating tuples
new_tuple = my_tuple + (6, 7)
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)

# Replicating tuples
replicated_tuple = my_tuple * 3
print(replicated_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Checking membership
print(3 in my_tuple)  # Output: True
print(6 in my_tuple)  # Output: False

# Finding the length of a tuple
print(len(my_tuple))  # Output: 5

# Counting occurrences of an element
print(my_tuple.count(2))  # Output: 1

# Finding the index of an element
print(my_tuple.index(4))  # Output: 3


# methods for tuples: count & index

# count() - returns the number of times a specified value occurs in a tuple
print(my_tuple.count(2)) # output is 1 because 2 is only occuring once 

# index() - searches the tuple for a specified value and returns the first position/occurrence of the specified value
print(my_tuple.index(4)) # output is 3 because 4 is in the 3rd position of the tuple

print(len(my_tuple)) # returns length of tuple 
print(max(my_tuple)) # max number in tuple: 5 
print(min(my_tuple)) # min number in tuple: 1 
print(tuple([1,2,3,4,5])) # converts list into tuple 