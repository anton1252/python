colors = ('red' ,'green' ,'blue' ,'yellow' ,'pink' ,'purple')
a = input('Введите цвет которое хотите удалить')
colors = list(colors)
colors.remove(a)
colors = tuple(colors)
print(colors)
