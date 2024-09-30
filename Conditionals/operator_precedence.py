print(1 or 2 and 3) # True - 1
print(0 or 2 and 3) # True - 3  
print(1 or 0 and 3) # True - 1
print(1 or 2 and 0) # True - 1
print(0 or 0 and 3) # False - 0
print(0 or 2 and 0) # False - 0
print(1 or 0 and 0) # True - 1
print(0 or 0 and 0) # False - 0

print(1 and 2 or 3) # True - 2
print(0 and 2 or 3) # True - 3
print(1 and 0 or 3) # True - 3
print(1 and 2 or 0) # True - 2
print(0 and 0 or 3) # True - 3
print(0 and 2 or 0) # False - 0 
print(1 and 0 or 0) # False - 0
print(0 and 0 or 0) # False - 0