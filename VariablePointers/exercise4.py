# What will this print and why?

# Because dict1[a] has a nested list as a value 
# in the outermost level there is a pointer to the 
# list [1, 2, 3] for the key 'a'
# In the assignment of dict2, a new dictionary object 
# is created but it is a shallow copy as 'a': pointer to [1, 2, 3]
# So dict1[a] and dict2[a] reference the same nested list 

# It will print [1, 42, 3]

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])