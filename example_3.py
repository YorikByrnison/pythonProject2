num = 3491561
num_1 = -1
while num > 10:
    delenie = num % 10
    num //= 10
    if delenie > num_1:
        num_1 = delenie
print(num_1)
