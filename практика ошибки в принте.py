try:
    age = int(input('Сколько тебе лет?: '))
except ValueError: 
    print('Введите ответ числом')
else:
    print('Ваш возраст:', age)
finally:
    print('Программа успешно завершена')
    
