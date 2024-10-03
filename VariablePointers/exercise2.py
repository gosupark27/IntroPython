# What will this print and why?

# The reference to the set object in set1 is copied to set2 
# set1 and set2 reference the same object
# the change made by set1 with adding the range element will
# be shown when printing out set2 

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)          # {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}

