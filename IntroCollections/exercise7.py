def print_range(my_range):
    print(list(my_range))


# [0, 1, 2, 3, 4, 5, 6]
print_range(range(7))

# [1, 2, 3, 4, 5]
print_range(range(1, 6))

# [3, 7, 11]
print_range(range(3, 15, 4))

# [] - empty because start < stop and the step is negative 
print_range(range(3, 8, -1))

# [8, 7, 6, 5, 4]
print_range(range(8, 3, -1))

