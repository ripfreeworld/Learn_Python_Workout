# Flip a dictionary

d = {'a':1, 'b':2, 'c':3}

flipped_d = { value : key
              # <expression> for <member> in <iterable>
              for key, value in d.items() }
              # All iterables are acceptable in a comprehension. 
              # Even those that return 2-element tuples, such as dict.items.
              
print(flipped_d)