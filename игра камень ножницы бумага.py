import random, time
print('Васап, ты попал в игру камень ножницы бумага!')
time.sleep(2)
print('Твоя цель обыграть бота, набрав 3 очка!')
time.sleep(2)
print('В каждом из твоих ходов ты должен выбрать камень ножницы или бумага')
time.sleep(2)
print('3!')
time.sleep(2)
print('2!')
time.sleep(2)
print('1!')
time.sleep(1)
print('ПОЕХАЛИ!')
userScore = 0
botScore = 0
botList = ['Камень', 'Ножницы', 'Бумага']
while userScore != 3 and botScore != 3:
    print('Новый раунд начался!')
    userChoose = input('Введите: камень, ножницы либо бумага: ').lower()
    botChoose = random.choice(botList).lower()
    print('Вы выбрали:', userChoose)
    print('Бот выбрал:', botChoose)
    if userChoose == botChoose:
        print('Ничья')
    elif botChoose == 'камень' and userChoose == 'ножницы':
        print('Выиграл бот')
        botScore += 1
    elif botChoose == 'камень' and userChoose == 'бумага':
        print('Выиграл пользователь')
        userScore += 1
    elif botChoose == 'ножницы' and userChoose == 'бумага':
        print('Выиграл бот')
        botScore += 1
    elif botChoose == 'ножницы' and userChoose == 'камень':
        print('Выиграл пользователь')
        userScore += 1
    elif botChoose == 'бумага' and userChoose == 'камень':
        print('Выиграл бот')
        botScore += 1
    elif botChoose == 'бумага' and userChoose == 'ножницы':
        print('Выиграл пользователь')
        userScore += 1
    else:
        print('Не удалось подвести итоги раунда')
    print('Счёт пользователя:', userScore)
    print('Счёт бота:', botScore)
if userScore > botScore:
    print('Победил пользователь со счётом:', userScore)
elif userScore < botScore:
    print('Победил бот со счётом:', botScore)
    

    


    
