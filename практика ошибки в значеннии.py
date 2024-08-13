try:
    loveNumber = int(input('Введите своё любимое число'))
except ValueError:
    print('Введите ответ числом')
else:
    if loveNumber >= 50:
        print('Ваше число больше или равно 50')
    else:
        print('Ваше число меньше 50')
finally:
    print('Ваша программа закончена')
        
        
        
    
