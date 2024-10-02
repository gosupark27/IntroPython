names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = list()
index = 0

# for loop equivalent 
for name in names: 
    if name.casefold == 'Max'.casefold: 
        continue
    upper_names.append(name.upper())
print(upper_names)

# Using a while loop

# while index < len(names):
#     upper_names.append(names[index].upper())
#     index += 1
# print(upper_names)