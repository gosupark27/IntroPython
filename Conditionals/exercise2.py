def even_or_odd(num):
    isEven = bool(not(num % 2))
    return 'even' if isEven else 'odd'

num = int(input("Enter a number: "))
print(even_or_odd(num))
