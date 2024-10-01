#Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')
print(f"tuple stuff: {stuff}")
temp_stuff = list(stuff)
temp_stuff[2] = 'goodbye'
stuff = tuple(temp_stuff)
print(f"modified tuple stuff: {stuff}")
