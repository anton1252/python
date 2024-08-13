try:
    a = int(input('Введите число:'))
except ValueError:
    print('Введите ответ числом')
else:
    print('Ваше число:', a**2)
finally:
    print('Операция завершена')
