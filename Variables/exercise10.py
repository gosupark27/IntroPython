# Reassignment, mutation, or neither? 

obj = 'ABcd'                # reassignment 
obj.upper()                 # neither 
obj = obj.lower()           # reassignment
print(len(obj))             # neither 
obj = list(obj)             # reassignment 
obj.pop()                   # mutation but you are removing an element...however lists are mutable 
obj[2] = 'X'                # mutation
obj.sort()                  # mutation
set(obj)                    # neither because the new set object is not bounded to obj            
obj = tuple(obj)            # reassignment creating a new tuple object