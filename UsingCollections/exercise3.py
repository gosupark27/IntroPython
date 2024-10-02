# Write Python code to create a new tuple from (1, 2, 3, 4, 5). 
# The new tuple should be in reverse order from the original. 
# It should also exclude the first and last members of the original. 
# The result should be the tuple (4, 3, 2)

my_tuple = (1, 2, 3, 4, 5)
my_tuple = list(reversed(my_tuple))[1:len(my_tuple)-1]
print(tuple(my_tuple))

my_tuple = (1, 2, 3, 4, 5)
reversed_list = list(reversed(my_tuple))
reversed_list.remove(1)
reversed_list.remove(5)
my_tuple = tuple(reversed_list)
print(my_tuple)
