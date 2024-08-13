my_dict = {'Milk':99, 'Orange':69, 'Banana':57, 'Juice':150}
my_dict_values = list(my_dict.values())
overPrice = 0
for i in my_dict_values:
  if i >= overPrice:
      overPrice = i
print(overPrice)
