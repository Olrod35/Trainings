import random
secretNumber = random.randint(1, 20)
print("задумано число от 1 до 20. Попробуйте угадать")

for guessesTaken in range(1, 6):
    print("Ваш вариант: ")
    guess = int(input())

    if guess < secretNumber:
        print("Число должно быть больше предложенного")
    elif guess > secretNumber:
        print("Число должно быть меньше предложенного")
    else:
        break

if guess == secretNumber:
    print("Верно! Количество попыток: " + str(guessesTaken))
else:
    print('Нет, было задумано число ' + str(secretNumber))
