# Flip a dictionary
# visualization view: http://pythontutor.com/visualize.html#mode=display

d = {'a':1, 'b':2, 'c':3}

flipped_d = { value : key
              # <expression> for <member> in <iterable>
              for key, value in d.items() }
              # All iterables are acceptable in a comprehension. 
              # Even those that return 2-element tuples, such as dict.items.
              
print(flipped_d)

# Another example of comprehension:
squares = [i * i for i in range(10)]
# congruent:
squares = []
for i in range(10):
    squares.append(i * i)

# nested loops create a Cartesian Product of the two sequences
# https://stackoverflow.com/questions/18649884/python-list-comprehension-for-loops

