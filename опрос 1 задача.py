a = int(input('Введите количество чисел которые будут в строке'))
my_list = []
for i in range(a):
    b = int(input('Введите значение списка'))
    if b >= 0:
        my_list.append(b)
c = len(my_list)
print(c)
