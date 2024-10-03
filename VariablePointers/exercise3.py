# What will this code print and why?

# It will print out 'The Life of Brian' 
# In the assignment of dict2, a new dictionary object 
# was created and dict2 is referencing a different object 
# So the change made to the 'Monty Python' key in dict2 
# will not be shown when dict1['Monty Python] is called

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])
print(dict1 is dict2)