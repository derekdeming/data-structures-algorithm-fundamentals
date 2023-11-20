
# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

# Traverse the tuple using a for loop
for element in my_tuple:
    print(element)

for i in range(len(my_tuple)):
    print(my_tuple[i])


# Traverse the tuple using a while loop
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1

# Traverse the tuple using tuple unpacking
a, b, c, d, e = my_tuple
print(a)
print(b)
print(c)
print(d)
print(e)

# Traverse the tuple using enumerate()
for index, element in enumerate(my_tuple):
    print(f'Index: {index}, Element: {element}')


# time complexity: O(n)
# space complexity: O(1)