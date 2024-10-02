text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# Why does it print different values?
# Line 3 is slicing the string first before calling rfind so the index of 0 will begin at the start of the sliced string 
# Line 4 is searching for the rightmost f between index 21 and 35 