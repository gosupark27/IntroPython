# Bob expects the following code to print the names in alphabetical order. 
# Without running the code, can you say whether it will? Explain your answer.

# It will not print the names in alphabetical order because a set, by definition, 
# is unordered so there is no guarantee. To have it printed in order use sorted() 
# which will alphabetize it and convert it to a list, which is an ordered collection 

names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)
print(sorted(names))