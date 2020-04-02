for i, item in enumerate('abc'):
    print (i, item)

my_dict = {i: i * i for i in range(10)} 
my_set = {i * 10 for i in range(10)} 
# somehow random order with "* 10"


print(my_dict)
print(my_set)