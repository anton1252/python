my_tuple = ('a', 5, 's', [1, 2, 3])
my_list = list(my_tuple)
my_list.insert(2, 3)
my_list.remove('a')
my_tuple = tuple(my_list)
print(my_tuple)
