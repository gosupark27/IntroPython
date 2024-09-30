# use function to determine which list contains a number not divisble by 3

def remainders_3(numbers):
    return [number % 3 for number in numbers]

def isNotDivisible(list):
    isDivisible = any(remainders_3(list))
    print(f"{list} does contain a number not divisible by 3: {isDivisible}")

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

isNotDivisible(numbers_1)
isNotDivisible(numbers_2)
isNotDivisible(numbers_3)
isNotDivisible(numbers_4)

