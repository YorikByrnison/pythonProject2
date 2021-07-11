start = int(input('сколько километров в первый день вы пробежали - '))
finish = int(input('сколько километров вы хотели бы пробегать - '))
day = 1

while finish - start > 0:
    start = start + (start * 0.1)
    day += 1

print(day)