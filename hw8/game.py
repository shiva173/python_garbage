from random import randint


def play():
    user_number = None
    min_number = 1
    max_number = 100
    number_start = min_number
    number_stop = max_number
    attempts = 0

    controller = {
        'small': '<',
        'big': '>',
        'right': 'true'
    }

    while True:
        user_number = input(f'Введите загаданное число от {min_number} до {max_number}: ')
        if not user_number.isdigit():
            print('Вы ввели не число!')
        elif not min_number <= int(user_number) <= max_number:
            print('Вы ввели число за пределами указанного диапазона!')
        else:
            user_number = int(user_number)
            break

    print('Сейчас компьютер начнет угадывать ваше число....')
    print(
        f"Управление в игре (если число компьютера больше: {controller['big']} если меньше {controller['small']} если равно {controller['right']})")

    operand = None
    while operand != controller['right']:
        random_number = randint(number_start, number_stop)
        attempts += 1

        while True:
            operand = input(f'Число {random_number} больше, меньше или равно загаданному? \n')
            if (random_number > user_number and operand == controller['big']) \
                    or (random_number < user_number and operand == controller['small']) \
                    or (random_number == user_number and operand == controller['right']):
                if operand == controller['big']:
                    number_stop = random_number - 1
                elif operand == controller['small']:
                    number_start = random_number + 1
                break
            else:
                print("Вы ошиблись при вводе проверьте себя пожалуйста и повторите ввод.")

    print(f"Компьютер угадал ваще число({user_number}) с {attempts} попытки!")
