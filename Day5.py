# Python Lists

# Creating a list
my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")

# Accessing elements
first_element = my_list[0]
print(f"First element: {first_element}")

last_element = my_list[-1]
print(f"Last element: {last_element}")

# Modifying elements
my_list[0] = 10
print(f"Modified list: {my_list}")

# Slicing a list
sub_list = my_list[1:3]
print(f"Sliced list: {sub_list}")

# Appending to a list
my_list.append(6)
print(f"List after appending: {my_list}")

# Removing from a list
my_list.remove(10)
print(f"List after removing: {my_list}")

# List comprehension
squared_list = [x ** 2 for x in my_list]
print(f"Squared list: {squared_list}")
