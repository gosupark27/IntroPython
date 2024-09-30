# What does the code print
# As exercise 5 won't print anything but this time it is because print(words) will not be executed since the function terminates on the line before it 

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')