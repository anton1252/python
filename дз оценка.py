try:
    bal = int(input("Введите свою оценку по 100бальной шкале"))
except ValueError:
    print('Введите ответ числом')
else:
    if bal <= 30:
        print('Ты можешь лучше')
    elif bal <=50:
        print("Удолетворительно")
    elif bal <=70:
        print("Хорошая работа")
    elif bal <=90:
        print("Отличная работа")
    else:
        print('Замечательная работа')
    
