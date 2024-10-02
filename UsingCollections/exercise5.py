# Which of the following values can't be used as a key in a dict object, and why?

# Keys can only be immutable types 

'cat'                                # Yes, str is immutable type     
(3, 1, 4, 1, 5, 9, 2)                # Yes, tuple is immutable
['a', 'b']                           # No, list is mutable   
{'a': 1, 'b': 2}                     # No, dictionary is mutable  
range(5)                             # Yes, range is immutable
{1, 4, 9, 16, 25}                    # No, set is mutable 
3                                    # Yes, int is immutable  
0.0                                  # Yes, float is immutable     
frozenset({1, 4, 9, 16, 25})         # Yes, frozen set is immutable     