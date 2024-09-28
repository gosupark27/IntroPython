# Using explicit type coercion to return an int, i.e., 3.1415
# However, this cannot happen since the string literal is a float (is not a whole number)
# ValueError: invalid literal for int() with base10

isInt = int('3.1415')
print(f"{{int('3.1415')}} will return an int: {type(isInt) is int}")