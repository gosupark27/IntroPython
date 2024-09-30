# What is the output of this code
# Prints Empty because an empty list is falsy so else block is executed 

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])