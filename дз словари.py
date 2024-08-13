a = int(input('Введите количество раз'))
dict = {}
for i in range(a):
     b = input('Введите слово')
     c = input('Введите слово')
     dict.update({b:c})
dict_keys = list(dict.keys())
d = input('Введите слово которое хотите найти')
for i in dict_keys:
     if i == d:
          print(dict[i])
          break
     elif dict[i] == d:
          print(i)
          break
else:
     print('Совпоподений не найдено ERRROOOOOORRRRRRRR')
