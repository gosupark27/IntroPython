# What does the following function do? Be sure to identify the output value.

# do_something sorts the keys of the dictionary in alphabetical order 
# and then returns the second element from the keys list
# CHRIS
# sorted key list: ['Antonina', 'CHRIS', 'Clare', 'Karis', 'Karl', 'Trevor']

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))