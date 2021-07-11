rev = int(input('Введите выручку вашей организации - '))
cost = int(input('Введите издержки вашей организации - '))
people = int(input('Сколько сотрудников работает в вашей организации - '))
amount = rev - cost


if rev > cost:
    print('Ваша компания в плюсе')
    amount > 1
    print('Ваша фирма рентабельна')
else:
    cost > rev
    print('Ваша компания в минусе и не рентабельна')

money = amount / people
print('На одного сотрудника приходится по', money, 'рублей прибыли')


