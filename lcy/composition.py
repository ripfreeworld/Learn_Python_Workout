class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    def __init__(self):
        self.scoops = []    # object to be a list

    def add_scoops(self, *new_scoops):
    # new_scoops will be a tuple containing 
    # all of the arguments that were passed to add_scoops
        for one_scoop in new_scoops:
            self.scoops.append(one_scoop)

    def __repr__(self):
        return ', '.join(s.flavor for s in self.scoops)
        # str.join(sequence)
        # add ", " in between string sequence

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b)                  # prints each flavor on a new line
# This has the effect of calling the __repr__ method on our object, 
# assuming that one is defined.
