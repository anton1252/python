import time
import random as rnd
print('Привет! Ты попал в игру "Почини мотоцикл"')
time.sleep(4)
print('Тебе стоит играть от лица подростка который нашел в гараже мотоцикл но он оказался сломаный')
time.sleep(4)
print('Тебе нужно выбрать чем починить ту деталь в мотоцикле которая сломана')
time.sleep(4)
print('Учти что за неправильный выбор ты не сможешь починить мотоцикл и будет GAME OVER')
time.sleep(4)
print('Ну, а если сделаешь правильный выбор то ты починишь ту деталь которую делал')
time.sleep(4)
print('После ты перейдешь к починке другой детали')
time.sleep(4)
print('Учти!')
time.sleep(4)
print('Мотоцикл ошибок не прощает')
score = 0

all_breaks = ['Замена лапки КПП', 'Замена кик стартера', 'Замена свечи', 'Замена камеры', 'Заправка']
breaks = []
random_count = rnd.randint(2,4)
for i in range(1, random_count + 1):
    random_element = rnd.choice(all_breaks)
    all_breaks.remove(random_element)
    breaks.append(random_element)
for i in breaks:
    
    if i == 'Замена лапки КПП':
        print('Замена лапки КПП')
        print('Чем будем менять?')
        print('1.Трещёткой 2.Вытащишь без открутки')
        user_input = int(input('Введите 1 или 2'))
        if user_input == 1:
            print('Вы успено заменили лапку КПП')
        else:
            print('Вы сорвали резьбу. Замена лапки КПП завершена неудачно')
            print('Игра завершена')
            break
    
        time.sleep(2)
    elif  i == 'Замена кик стартера':
        print('Замена кик стартера')
        print('Чем будем менять?')
        print('1.Трещёткой 2.Вытащишь без открутки')
        user_input = int(input('Введите 1 или 2'))
        if user_input == 1:
            print('Вы успено заменили кик стартер')
        else:
            print('Вы сорвали резьбу. Замена кик стартера завершена неудачно')
            print('Игра завершена')
            break
    
        time.sleep(2)
    elif i == 'Замена свечи':
        print('Замена свечи')
        print('Чем будем менять?')
        print('1.Свечным ключом 2.Вырву рукой')
        user_input = int(input('Введите 1 или 2'))
        if user_input == 1:
            print('Вы успено заменили свечу')
        else:
            print('Вы сорвали резьбу в головке двигателя и саму свечу. Замена свечи завершена неудачно')
            print('Игра завершена')
            break
    
        time.sleep(2)
    elif i == 'Замена камеры':
        print('Замена камеры')
        print('Чем будем менять?')
        print('1.Ломом 2.Ножом')
        user_input = int(input('Введите 1 или 2'))
        if user_input == 1:
            print('Вы успено заменили камеру')
        else:
            print('Вы проткнули камеру. Замена камеры завершена неудачно')
            print('Игра завершена')
            break
    
        time.sleep(2)
    elif i == 'Заправка':
        print('Заправка')
        print('Чем будем заправлять?')
        print('1.92 бензом 2.Дизелем')
        user_input = int(input('Введите 1 или 2'))
        if user_input == 1:
            print('Вы успено заправили мотоцикл')
        else:
            print('У вас отрыгнул мотор. Заправка неудачна.')
            print('Игра завершена')
            break
else:
    print('Игра завершена. Мотоцикл починен!!!')
        
