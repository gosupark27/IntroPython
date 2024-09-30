# What does this code print?
# Prints out Product2 and Product not found! because bar_code_scanner(142) passes an integer value as an argument when 
# the match statement is comparing string values. Hence, the default case is given for this function call. 

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)