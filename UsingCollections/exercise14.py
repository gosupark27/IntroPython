# Assume following sequences

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

# Write some code that combines the sequences into a list of tuples. 
# Each tuple should contain one member of each sequence. 
# Print the final result so you can see all the values, which should look like this:

list_of_tuples = zip(my_str, my_list, my_tuple, my_range)
print(list(list_of_tuples))