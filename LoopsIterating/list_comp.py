squares = list()
for num in range(5):
    square = num * num
    squares.append(square)

print(squares)

squares_comp = [num * num for num in range(5)]
print(squares_comp)

even_squares = [num * num for num in range(20)
                if num % 2 == 0]
print(even_squares)

cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

cat_names = [name.upper() for name, color in cats_colors.items()
             if color.lower() == 'orange'
             if name[0].upper() == 'L']
print(cat_names)