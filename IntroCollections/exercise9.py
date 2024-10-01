my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Are the lists assigned to my_list and another_list equal?
# Yes, they are equal 
print(f"Is my_list equal to another_list: {my_list == another_list}")

# Are the lists assigned to my_list and another_list the same object?
# No, they are not the same object 
print(f"Is my_list and anoter_list the same object: {my_list is another_list}")

# Are the nested lists at index 3 of my_list and another_list equal?
# Yes, they are equal. They both contain the same elements 
print(f"Is the nested list at index 3 of my_list and another_list equal: {my_list[3] == another_list[3]}")

# Are the nested lists at index 3 of my_list and another_list the same object?
# Yes, the nested list at index 3 are equal because nested lists use shallow copy so a reference to the nested list gets copied 
print(f"Is the nested list at index 3 of my_list and another_list the same object: {my_list[3] is another_list[3]}")
