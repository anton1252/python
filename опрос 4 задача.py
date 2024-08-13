my_dict = {'Ann':80,'Nikolay':40,'Sofia':55,'Lena':35,'Petr':90,'Misha':60,}
a = int(input('Введите проходной балл'))
dict_keys = list(my_dict.keys())
for i in dict_keys:
    if my_dict(i) <= a:
        del my_dict(i)
print(my_dict)
        
