# Determine what gets printed

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats)         # True   
print('Butter' in cats)               # False
print('Butter' in cats[3])            # True; comparing 'Butter' to 'Butterscotch' instead of collection so as long as it is a substring
print('cheddar' in cats)              # False; case sensitive 