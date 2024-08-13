a = int(input('Введите средний бал'))
my_dict = {'Ksusha':100, 'Danil':25, 'Nikolay':55, 'Matvey':10}
my_dict_keys = list(my_dict.keys())
for i in my_dict_keys:
    if my_dict[i] > a:
        print(my_dict[i])
